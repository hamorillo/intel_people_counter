import cv2
import tensorflow as tf
import time
import statistics
from argparse import ArgumentParser

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

    return parser

def infer_on_stream(args):
    
    cap = cv2.VideoCapture()
    cap.open(args.input)

    inference_times = []

    with tf.Session() as sess:
        # We load the model and its weights
        # Models from the zoo are frozen, so we use the SERVING tag
        model = tf.saved_model.loader.load(sess, 
                                [tf.saved_model.tag_constants.SERVING], 
                                args.model)
        # we get the model signature
        model_signature = model.signature_def["serving_default"]
        input_tensor = model_signature.inputs["inputs"].name
        # getting the name of the outputs
        output_tensor = [v.name for k,v in model_signature.outputs.items() if v.name]
        
        while cap.isOpened():
            flag, frame = cap.read()
            
            if not flag:
                break

            # running the prediction
            time_start = int(round(time.time() * 1000))
            outs = sess.run(output_tensor, feed_dict={input_tensor:[frame]})
            time_end = int(round(time.time() * 1000))
            inference_times.append(time_end-time_start)

        
        print("Average Time:" + str(statistics.mean(inference_times)))

def main():
    # Grab command line args
    args = build_argparser().parse_args()
    # Perform inference on the input stream
    infer_on_stream(args)

if __name__ == '__main__':
    main()