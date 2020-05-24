# Project Write-Up - Models

## SSD_Mobilenet v2 COCO - TensorFlow
http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_coco_2018_03_29.tar.gz  
Model Optimizer Command:  
`python3 /opt/intel/openvino/deployment_tools/model_optimizer/mo_tf.py --input_model frozen_inference_graph.pb --reverse_input_channels --tensorflow_object_detection_api_pipeline_config pipeline.config --tensorflow_use_custom_operations_config /opt/intel/openvino/deployment_tools/model_optimizer/extensions/front/tf/ssd_v2_support.json` 

## COCO SSD512* - Caffe
https://github.com/weiliu89/caffe/tree/ssd#models  
Direct URL: https://drive.google.com/open?id=0BzKzrI_SkD1_dlJpZHJzOXd3MTg  
Model Optimizer Command:  
 `python /opt/intel/openvino/deployment_tools/model_optimizer/mo.py --input_model models/VGGNet/coco/SSD_512x512/VGG_coco_SSD_512x512_iter_360000.caffemodel --input_proto /Users/hector/Downloads/intel/models/VGGNet/coco/SSD_512x512/deploy.prototxt`
 
## COCO SSD300* - Caffe
https://github.com/weiliu89/caffe/tree/ssd#models  
Direct URL: https://drive.google.com/open?id=0BzKzrI_SkD1_dUY1Ml9GRTFpUWc  
Model Optimizer Command:  
 `python /opt/intel/openvino/deployment_tools/model_optimizer/mo.py --input_model models/VGGNet/coco/SSD_300x300/VGG_coco_SSD_300x300_iter_400000.caffemodel --input_proto /Users/hector/Downloads/intel/models/VGGNet/coco/SSD_300x300/deploy.prototxt`

## VOC SSD300* - Caffe
https://github.com/weiliu89/caffe/tree/ssd#models  
Direct URL: https://drive.google.com/open?id=0BzKzrI_SkD1_TkFPTEQ1Z091SUE
Model Optimizer Command:  
 `python /opt/intel/openvino/deployment_tools/model_optimizer/mo.py --input_model models/VGGNet/SSD_300x300_ft/VGG_VOC0712Plus_SSD_300x300_ft_iter_160000.caffemodel --input_proto /Users/hector/Downloads/intel/models/VGGNet/SSD_300x300_ft/deploy.prototxt`

## COCO SSD Inception v2 - TensorFlow  
http://download.tensorflow.org/models/object_detection/ssd_inception_v2_coco_2018_01_28.tar.gz  
Model Optimizer Command:  
`python3 /opt/intel/openvino/deployment_tools/model_optimizer/mo_tf.py --input_model frozen_inference_graph.pb --reverse_input_channels --tensorflow_object_detection_api_pipeline_config pipeline.config --tensorflow_use_custom_operations_config /opt/intel/openvino/deployment_tools/model_optimizer/extensions/front/tf/ssd_v2_support.json` 

## COCO SSD Mobilenet  v1 - TensorFlow
http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_fpn_shared_box_predictor_640x640_coco14_sync_2018_07_03.tar.gz  
Model Optimizer Command:  
`python3 /opt/intel/openvino/deployment_tools/model_optimizer/mo_tf.py --input_model frozen_inference_graph.pb --reverse_input_channels --tensorflow_object_detection_api_pipeline_config pipeline.config --tensorflow_use_custom_operations_config /opt/intel/openvino/deployment_tools/model_optimizer/extensions/front/tf/ssd_v2_support.json` 

## SSD-ResNet-50 - MXNet
**NOT WORKING**  
https://gluon-cv.mxnet.io/model_zoo/detection.html#faster-rcnn  
Model Optimizer Command:  
 `python /opt/intel/openvino/deployment_tools/model_optimizer/mo_mxnet.py --input_model models/ssd_512_resnet50_v1_voc-9c8b225a/ssd_512_resnet50_v1_voc-9c8b225a.params --enable_ssd_gluoncv`

 *Always return the same error:*
 >[ ERROR ]  Exception occurred during running replacer "REPLACEMENT_ID" (<class 'extensions.load.mxnet.loader.MxNetLoader'>): Input model name /Users/hector/Downloads/intel/models/yolo3_darknet53_voc-f5ece5ce.params is not in an expected format, cannot extract iteration number. 
 For more information please refer to Model Optimizer FAQ (https://docs.openvinotoolkit.org/latest/_docs_MO_DG_prepare_model_Model_Optimizer_FAQ.html), question #48.

## Faster RCNN Resnet101 Kitti
**NOT WORKING**  
http://download.tensorflow.org/models/object_detection/faster_rcnn_resnet101_kitti_2018_01_28.tar.gz  
Model Optimizer Command:  
`python3 /opt/intel/openvino/deployment_tools/model_optimizer/mo_tf.py --input_model frozen_inference_graph.pb --reverse_input_channels --tensorflow_object_detection_api_pipeline_config pipeline.config --tensorflow_use_custom_operations_config /opt/intel/openvino/deployment_tools/model_optimizer/extensions/front/tf/faster_rcnn_support.json`
 
>[ WARNING ] Model Optimizer removes pre-processing block of the model which resizes image keeping aspect ratio. The Inference Engine does not support dynamic image size so the Intermediate Representation file is generated with the input image size of a fixed size.
Specify the "--input_shape" command line parameter to override the default shape which is equal to (600, 600).  
The Preprocessor block has been removed. Only nodes performing mean value subtraction and scaling (if applicable) are kept.  
The graph output nodes "num_detections", "detection_boxes", "detection_classes", "detection_scores" have been replaced with a single layer of type "Detection Output". Refer to IR catalogue in the documentation for information about this layer.  
[ WARNING ]  Network has 2 inputs overall, but only 1 of them are suitable for input channels reversing.  
Suitable for input channel reversing inputs are 4-dimensional with 3 channels
All inputs: {'image_tensor': [1, 3, 600, 600], 'image_info': [1, 3]}
Suitable inputs {'image_tensor': [1, 3, 600, 600]}

I notice that the model has two inputs and I adapted the code to use the input `image_tensor`and reshape the input to (600, 600) but when I try to execute I always get a segmentation faul error like this:

>Segmentation fault: 11

**Note**: Same case happened with [faster_rcnn_resnet101_coco](http://download.tensorflow.org/models/object_detection/faster_rcnn_resnet101_coco_2018_01_28.tar.gz)