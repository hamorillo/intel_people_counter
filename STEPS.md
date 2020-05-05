# Deploy a People Counter App at the Edge
## Inference

- [ ] Convert a Model into an Intermediate Representation with the Model Optimizer

**First Model**

Repo: https://github.com/davidsandberg/facenet
Model Optimizer Command:
`python3 /opt/intel/openvino/deployment_tools/model_optimizer/mo_tf.py --input_model 20180402-114759.pb  --freeze_placeholder_with_value "phase_train->False" --reverse_input_channels`

Repo: http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v2_coco_2018_03_29.tar.gz
Model Optimizer Command:
`python3 /opt/intel/openvino/deployment_tools/model_optimizer/mo_tf.py --input_model frozen_inference_graph.pb --reverse_input_channels --tensorflow_object_detection_api_pipeline_config pipeline.config --tensorflow_use_custom_operations_config /opt/intel/openvino/deployment_tools/model_optimizer/extensions/front/tf/ssd_v2_support.json` 

- [ ] Load the Model Intermediate Representation into the Inference Engine
- [ ] Check for Custom Layers
- [ ] Handle Inference Requests Asynchronously
- [ ] Return Appropriate Results