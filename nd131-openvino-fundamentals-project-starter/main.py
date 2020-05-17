"""People Counter."""
"""
 Copyright (c) 2018 Intel Corporation.
 Permission is hereby granted, free of charge, to any person obtaining
 a copy of this software and associated documentation files (the
 "Software"), to deal in the Software without restriction, including
 without limitation the rights to use, copy, modify, merge, publish,
 distribute, sublicense, and/or sell copies of the Software, and to
 permit person to whom the Software is furnished to do so, subject to
 the following conditions:
 The above copyright notice and this permission notice shall be
 included in all copies or substantial portions of the Software.
 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
 LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
 OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
 WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


# MQTT server environment variables


import os
import sys
import time
import socket
import json
import cv2
import random
import numpy as np
import logging as log
import logging.handlers
import paho.mqtt.client as mqtt
from argparse import ArgumentParser
from inference import Network
HOSTNAME = socket.gethostname()
IPADDRESS = socket.gethostbyname(HOSTNAME)
MQTT_HOST = IPADDRESS
MQTT_PORT = 3001
MQTT_KEEPALIVE_INTERVAL = 60

INPUT_CAMERA = "CAMERA"
INFERENCE_TOLERANCE_FRAMES = 30
IMAGE_SET_COCO = "COCO"
IMAGE_SET_PASCAL_VOC = "PASCAL_VOC"


def init_logger(file_path):
    log.getLogger().setLevel(log.NOTSET)
    handler = logging.FileHandler(file_path)
    handler.setFormatter(log.Formatter(
        '%(asctime)s - %(levelname)s: %(message)s'))
    handler.setLevel(level=log.DEBUG)
    log.getLogger().addHandler(handler)


def build_argparser():
    """
    Parse command line arguments.

    :return: command line arguments
    """
    parser = ArgumentParser()
    parser.add_argument("-m", "--model", required=True, type=str,
                        help="Path to an xml file with a trained model.")
    parser.add_argument("-i", "--input", required=True, type=str,
                        help="Path to image or video file")
    parser.add_argument("-l", "--cpu_extension", required=False, type=str,
                        default=None,
                        help="MKLDNN (CPU)-targeted custom layers."
                             "Absolute path to a shared library with the"
                             "kernels impl.")
    parser.add_argument("-d", "--device", type=str, default="CPU",
                        help="Specify the target device to infer on: "
                             "CPU, GPU, FPGA or MYRIAD is acceptable. Sample "
                             "will look for a suitable plugin for device "
                             "specified (CPU by default)")
    parser.add_argument("-pt", "--prob_threshold", type=float, default=0.5,
                        help="Probability threshold for detections filtering"
                        "(0.5 by default)")
    parser.add_argument("-lf", "--log_file", type=str, default='logs/' + time.asctime(time.localtime()) + '.log',
                        help="Specify the log file to use. For default each execution"
                        "will generate a new log file.")
    parser.add_argument("-tf", "--tolerance_frames", type=int, default=INFERENCE_TOLERANCE_FRAMES,
                        help="Specify the number of frames that we use as tolerance for errors."
                        "This values is used for detect when a person goes out of the frame.")
    parser.add_argument("-is", "--image_set", type=str, default=IMAGE_SET_COCO,
                        help="Specify the image set used, we will use this to determinate what"
                        "value indentify a person in the output. Ex: COCO = 1, PASCAL_VOC = 15")

    return parser


def connect_mqtt():
    ### TODO: Connect to the MQTT client ###
    mqttc = mqtt.Client()
    mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

    return mqttc


def is_person_detected(args, value_detected):
    if args.image_set == IMAGE_SET_COCO:
        return value_detected == 1
    elif args.image_set == IMAGE_SET_PASCAL_VOC:
        return value_detected == 15
    else:
        return None


def draw_boxes(frame, result, args, width, height):
    '''
    Draw bounding boxes onto the frame.
    '''
    people_in_frame = 0
    for box in result[0][0]:  # Output shape is 1x1x100x7
        conf = box[2]
        if is_person_detected(args, box[1]) and conf >= args.prob_threshold:
            people_in_frame += 1
            xmin = int(box[3] * width)
            ymin = int(box[4] * height)
            xmax = int(box[5] * width)
            ymax = int(box[6] * height)
            cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 0, 255), 1)
    return frame, people_in_frame


def is_image(path):
    '''
    Try to read the input file with the imread, if they return something difference from None,
    it means it is an image.
    '''
    image = cv2.imread(path)
    return image is not None


def output_image_path(path):
    return os.path.splitext(path)[0] + '_output' + os.path.splitext(path)[1]


def get_input_for_cv2(user_input):
    if(user_input == INPUT_CAMERA):
        return 0
    else:
        return user_input


def infer_on_stream(args, mqtt_client):
    """
    Initialize the inference network, stream video to network,
    and output stats and video.

    :param args: Command line arguments parsed by `build_argparser()`
    :param client: MQTT client
    :return: None
    """
    # Initialise the class
    infer_network = Network()
    # Set Probability threshold for detections
    prob_threshold = args.prob_threshold

    ### TODO: Load the model through `infer_network` ###
    infer_network.load_model(args.model, args.device, args.cpu_extension)

    single_image_mode = is_image(args.input)

    ### TODO: Handle the input stream ###
    cap = cv2.VideoCapture()
    cap.open(get_input_for_cv2(args.input))

    # Grab the shape of the input
    width = int(cap.get(3))
    height = int(cap.get(4))

    # Create a video writer for the output video
    # The second argument should be `cv2.VideoWriter_fourcc('M','J','P','G')`
    # on Mac, and `0x00000021` on Linux
    # out = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc('H','2','6','4'), 30, (width,height))

    total_people_count = 0
    frames_without_people = 5
    input_time = None

    ### TODO: Loop until stream is over ###
    while cap.isOpened():
        ### TODO: Read from the video capture ###
        flag, frame = cap.read()
        if not flag:
            break

        ### TODO: Pre-process the image as needed ###
        net_input_shape = infer_network.get_input_shape()

        p_frame = cv2.resize(frame, (net_input_shape[3], net_input_shape[2]))
        p_frame = p_frame.transpose((2, 0, 1))
        p_frame = p_frame.reshape(1, *p_frame.shape)

        ### TODO: Start asynchronous inference for specified request ###
        infer_network.exec_net(p_frame)

        ### TODO: Wait for the result ###
        if (infer_network.wait() == 0):
            ### TODO: Get the results of the inference request ###
            # Output Shape -> [1, 1, 100, 7] #
            result, infer_time = infer_network.get_output()

            ### TODO: Extract any desired stats from the results ###
            frame, people_in_frame = draw_boxes(
                frame, result, args, width, height)
            # Write out the frame
            # out.write(frame)

            ### TODO: Calculate and send relevant information on ###
            ### current_count, total_count and duration to the MQTT server ###
            ### Topic "person": keys of "count" and "total" ###
            ### Topic "person/duration": key of "duration" ###
            if(people_in_frame >= 1 and frames_without_people > args.tolerance_frames):
                total_people_count += 1
                frames_without_people = 0
                input_time = time.time()
            elif (people_in_frame == 0 and frames_without_people == args.tolerance_frames and input_time != None):
                person_duration = json.dumps(
                    {'duration': time.time()-input_time})
                mqtt_client.publish("person/duration",
                                    payload=person_duration, qos=0, retain=False)
                frames_without_people += 1
            elif people_in_frame == 0:
                frames_without_people += 1

            person = json.dumps(
                {'count': people_in_frame, 'total': total_people_count})

            mqtt_client.publish("person", payload=person, qos=0, retain=False)

            inference = json.dumps({'time': infer_time})            
            mqtt_client.publish("inference", payload=inference, qos=0, retain=False)

        ### TODO: Write an output image if `single_image_mode` ###
        if(single_image_mode):
            cv2.imwrite(output_image_path(args.input), frame)
        else:
            ### TODO: Send the frame to the FFMPEG server ###
            sys.stdout.buffer.write(frame)
            sys.stdout.flush()


def main():
    """
    Load the network and parse the output.

    :return: None
    """
    # Grab command line args
    args = build_argparser().parse_args()
    # Init logger
    init_logger(args.log_file)
    # Connect to the MQTT server
    mqtt_client = connect_mqtt()
    # Perform inference on the input stream
    infer_on_stream(args, mqtt_client)


if __name__ == '__main__':
    main()
