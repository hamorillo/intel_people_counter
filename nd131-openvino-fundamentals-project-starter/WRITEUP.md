# Project Write-Up
**Author**: Héctor Abraham Morillo Prieto

## Explaining Custom Layers

Custom layers are the way to thread with non directly supported layers in OpenVino from the original model. We could find custom layers through the Model Optimizer (layers that are not directly supported) and in execution time with the inference engine (depending on the hardware that we are using).

### Custom Layers on the Model Optimizer
When we are using the model optimizer over a model with non supported layers, any of this layers will automatically classified as a custom layer. 
Depending on the model framework we have difference ways of handle the custom layer, some of them are common to all frameworks, for example:
- Register an extension on the Model Optimizer
- Register the layer as custom and execute on the original model. This method imply that we need to have installed and ready the original framework in our system

Each framework could have other ways to handle with non supported layers, for example, Tensorflow allows to replace the unsupported subgraph with other subgraph.

### Non supported layer on a concrete hardware
When we are going to execute the Inference Engine with an Intermediate Representation we should verify in execution time if the hardware supports all the layers. Sometimes, our hardware couldn't manage some layer and we have to handle it. 

For example some layer are not supported in CPU's so we should use extensions for the Inference Engine in order to allow the execution of this model in that hardware. OpenVino toolkit provide us some extension for this kind of issues.

## Comparing Model Performance

My method(s) to compare models before and after conversion to Intermediate Representations
were...

In this project I try to select different pre-trained models in order to practice with the Model Optimizer and several machine learning frameworks. Some of the pre-trained models that I try to use gave me successfully results but others I would need more time to achieve better results.

You could find the models list with the link and the model Optimizer command [here](./WRITEUP-models.md)

As you could see on the list, I try to use different frameworks, image-sets and networks.

### Size Comparison

| Model                                            | Original Size  | IR Size      |
|:---:                                             |:---:           |:---:         |
| TF - SSD Mobilenet v2 COCO (2018_03_29)          | 69,7 mb        | 67,3 mb      |
| TF - SSD Inception v2 COCO (2018_01_28)          | 102 mb         | 100,1 mb     |
| CAFFE - COCO SSD512*                             | 144,2 mb       | 144,2 mb     |
| CAFFE - COCO SSD300*                             | 137,2 mb       | 137,2 mb     |
| CAFFE - VOC SSD300*                              | 105,2 mb       | 105,1 mb     |
| TF - SSD Mobilenet v1 FPN COCO (2018_07_03)\*    | **51,3 mb**    | **123,7 mb** |
| TF - Faster RCNN Resnet101 Kitti (2018_01_28)\*\*| 189,4 mb       | 188,9 mb**   |
| TF - Faster RCNN Resnet101 COCO (2018_01_28)\*\* | 196,5 mb       | 192,5 mb**   |

In almost every case I tested the original size is very similar than their Inference Representation after used the Model Optimizer. There is only one striking case the *TF - SSD Mobilenet v1 FPN COCO (2018_07_03)* where the difference between sizes is more than **72 mb**. I don't have a clear explanation for that so I may investigate more.

**\*Note:** I tried to optimize some MXNET / Gluon models but I didn't achieve it. You could see more detail in [used models file](./WRITEUP-models.md).  
**\*\*Note:** It was successfully converted but I couldn't make real inferences with it


### Accuracy 

As we discuss in some of the issues on the knowledge in Udacity, I assume that the accuracy pre- and post-conversion is the same.

### Inference time

The inference time of the model pre- and post-conversion was...

## Assess Model Use Cases

### Marketing Stands / Shop showcases
A good potential use case could in marketing stands or shop showcases. We could determine how many people stops in front of the marketing action and how much time they spend looking the advertisement. This data could be very useful if we are able to cross data with other information like the gender, the age, the location of the advertisement a any other data depending of what information are we looking for. 

For example we can test several marketing campaigns for one product (like an A/B test) and determinate which is more effectively and between what kind of person (young people, parents, etc). 

Maybe we could go further, and if we are in a fair a we could localize the person who is interested in our product (we can analyze the time they was looking our showcase), we can send some kind of promotion to them in order to encourage them to buy or get more information about the product.

Other possibility in the marketing field, if we are capable of re-identify a person a know how many times they come to see the showcase, we could make some kind of action that they could see to encourage to purchase our product or service.

### Prevention of occupational hazards with heavy machine
Some times heavy machine is difficult to manage due to their size, they are big machines and is difficult for the drive be sure that if he realize some movement or actions nobody will be at risk. 

If we install cameras on this kind of heavy machines we could react with several actions if we detect the presence of a person. In fact, we could implement difference actions if the person just enter in the action radius of the machine, like an alarm, or block the machine if the spend more than a determinate number of seconds inside the danger zone.

### Improvement traffic lights management
The management of the traffic lights in a city is to difficult and it contribute to the global warming when we force to stop the traffic if nobody want's to cross the street. 

We could use or pedestrian detector in order to determinate when someone is waiting for crossing the street a use this information to regulate the traffic lights. With this approach, in the hour that there are less pedestrians in the street we avoid to stop the cars if it's not needed.

## Assess Effects on End User Needs

Lighting, model accuracy, and camera focal length/image size have different effects on a
deployed edge model. The potential effects of each of these are as follows...

## Model Research

[This heading is only required if a suitable model was not found after trying out at least three
different models. However, you may also use this heading to detail how you converted 
a successful model.]

In investigating potential people counter models, I tried each of the following three models:

- Model 1: [Name]
  - [Model Source]
  - I converted the model to an Intermediate Representation with the following arguments...
  - The model was insufficient for the app because...
  - I tried to improve the model for the app by...
  
- Model 2: [Name]
  - [Model Source]
  - I converted the model to an Intermediate Representation with the following arguments...
  - The model was insufficient for the app because...
  - I tried to improve the model for the app by...

- Model 3: [Name]
  - [Model Source]
  - I converted the model to an Intermediate Representation with the following arguments...
  - The model was insufficient for the app because...
  - I tried to improve the model for the app by...
