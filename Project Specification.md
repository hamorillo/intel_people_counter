# Deploy a People Counter App at the Edge
## Inference

- [ ] Convert a Model into an Intermediate Representation with the Model Optimizer
>A link to the original model is included, along with the command used in the terminal to convert it to an Intermediate Representation with the Model Optimizer. This can be noted in the project README or in the Submission Details section for the reviewer (on the submission page).  
>
>The model cannot be one of the existing Intermediate Representations provided by Intel®.  
>
>This should be included irrespective of the additional option to use one of the IR models if a suitably accurate model is not found (see Write-Up section).

**First Model**

Repo: (SSD_Mobilenet COCO - TensorFlow) http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_coco_2018_03_29.tar.gz
Model Optimizer Command:
`python3 /opt/intel/openvino/deployment_tools/model_optimizer/mo_tf.py --input_model frozen_inference_graph.pb --reverse_input_channels --tensorflow_object_detection_api_pipeline_config pipeline.config --tensorflow_use_custom_operations_config /opt/intel/openvino/deployment_tools/model_optimizer/extensions/front/tf/ssd_v2_support.json` 

Repo (COCO SSD512* - Caffe): https://github.com/weiliu89/caffe/tree/ssd#models
Model Optimizer Command:
 `python /opt/intel/openvino/deployment_tools/model_optimizer/mo.py --input_model models/VGGNet/coco/SSD_512x512/VGG_coco_SSD_512x512_iter_360000.caffemodel --input_proto /Users/hector/Downloads/intel/models/VGGNet/coco/SSD_512x512/deploy.prototxt`
 
Repo (COCO SSD300* - Caffe): https://github.com/weiliu89/caffe/tree/ssd#models
Model Optimizer Command:
 `python /opt/intel/openvino/deployment_tools/model_optimizer/mo.py --input_model models/VGGNet/coco/SSD_300x300/VGG_coco_SSD_300x300_iter_400000.caffemodel --input_proto /Users/hector/Downloads/intel/models/VGGNet/coco/SSD_300x300/deploy.prototxt`

Repo (VOC SSD300* - Caffe): https://github.com/weiliu89/caffe/tree/ssd#models
Model Optimizer Command:
 `python /opt/intel/openvino/deployment_tools/model_optimizer/mo.py --input_model models/VGGNet/SSD_300x300_ft/VGG_VOC0712Plus_SSD_300x300_ft_iter_160000.caffemodel --input_proto /Users/hector/Downloads/intel/models/VGGNet/SSD_300x300_ft/deploy.prototxt`
 
**NOT WORKING** :Repo (SSD-ResNet-50 - MXNet): https://gluon-cv.mxnet.io/model_zoo/detection.html#faster-rcnn
Model Optimizer Command:
 `python /opt/intel/openvino/deployment_tools/model_optimizer/mo_mxnet.py --input_model models/ssd_512_resnet50_v1_voc-9c8b225a/ssd_512_resnet50_v1_voc-9c8b225a.params --enable_ssd_gluoncv`

 *Always return the same error:*
 >[ ERROR ]  Exception occurred during running replacer "REPLACEMENT_ID" (<class 'extensions.load.mxnet.loader.MxNetLoader'>): Input model name /Users/hector/Downloads/intel/models/yolo3_darknet53_voc-f5ece5ce.params is not in an expected format, cannot extract iteration number. 
 For more information please refer to Model Optimizer FAQ (https://docs.openvinotoolkit.org/latest/_docs_MO_DG_prepare_model_Model_Optimizer_FAQ.html), question #48.
 

- [ ] Load the Model Intermediate Representation into the Inference Engine
>In `inference.py`, a person detection model is loaded using the Inference Engine.

- [X] Check for Custom Layers
>`inference.py` includes code that will notify the user that certain layers are not supported (if applicable), and allows for the use of a CPU extension in this case.
- [X] Handle Inference Requests Asynchronously
>Requests for inference are handled asynchronously through the Inference Engine.
- [ ] Return Appropriate Results
>The output of the network is appropriately returned through get_output().

## Processing Video

- [ ] Handle Different Input Streams

> In `main.py`, an input image or video file is handled appropriately, along with any potential webcam or similar streaming video.
>
>The user is notified if a given input is unsupported.

- [ ] Preprocess the Input
	
> Appropriate preprocessing has been performed on an input image frame for input into the inference network.

- [ ] Extract Information from Model Output
	
> The output of the network is appropriately processed, with bounding boxes/semantic masks extracted  from the output, as applicable.
>
>If using bounding boxes, it utilizes a probability threshold to toss out low confidence detections.

- [ ] Calculate Relevant Statistics
> Statistics regarding people on screen, duration they spend on screen, and total people counted are calculated based off of the detected bounding boxes/semantic masks.
>
>The logic above results in close to actual statistics (no more than +/- 1 on people or +/- 2 seconds for time spent on screen). 

## Sending Data to Servers
- [X] Statistics Sent to MQTT Server	
>The calculated statistics are sent through JSON to a MQTT server.
>
>In the classroom workspace, this should be on port 3001 and publish to topics person and person/duration. person should have the keys total for the total count and count for the current count, while person/duration should use a duration key for publishing information.

- [X] Image Frame Sent to FFmpeg Server	
>The image frame, including any drawn outputs, are flushed to a FFmpeg server.

- [X] Video and Statistics Viewable in UI	
>The video and statistics are viewable through a UI. This can either use the provided UI or one created by the student.

## Write-Up

- [ ] Explaining Custom Layers in OpenVINO™
>A write-up is provided that includes an explanation of the process behind converting any custom layers, as well as explaining the potential reasons for handling custom layers in a trained model.

- [ ] Compare Model Performance	
>Create and explain your method behind comparing the performance of a model with and without the use of the OpenVINO™ Toolkit (accuracy, size, speed, CPU overhead).
>
>Also, compare the differences in network needs and costs of using cloud services as opposed to deploying at the edge.

- [ ] Assess Model Use Cases
>Explain potential use cases of a people counter app.
>
>This should include more than just listing the use cases - explain how they apply to the app, and how they might be useful.

- [ ] Assess Effects on End User Needs
>Discuss lighting, model accuracy, and camera focal length/image size, and the effects these may have on an end user requirement.

- [ ] Documenting Model Research
>If a suitably accurate model is not found, and the student instead utilizes an existing Intermediate Representations provided by Intel®, at least three model attempts should be documented as follows:
>
>- Where the model was obtained from  
>- How to convert the model to an IR  
>- Why the model failed and attempts to get it to succeed, such as adjusting confidence threshold

## Suggestions to Make Your Project Stand Out!


- [ ] Add an alarm or notification when the app detects above a certain number of people on video, or people are on camera longer than a certain length of time.
- [ ] Try out different models than the People Counter, including a model you have trained. Note that this may require some alterations to what information is passed through MQTT and what would need to be displayed by the UI.
- [ ] Deploy to an IoT device (outside the classroom workspace or your personal computer), such as a Raspberry Pi with Intel® Neural Compute Stick.
- [ ] Add a recognition aspect to your app to be able to tell if a previously counted person returns to the frame. The recognition model could also be processed on a second piece of hardware.
- [ ] Add a toggle to the UI to shut off the camera feed and show stats only (as well as to toggle the camera feed back on). Show how this affects performance (including network effects) and power.