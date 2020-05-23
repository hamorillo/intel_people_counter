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

The difference between model accuracy pre- and post-conversion was...

The size of the model pre- and post-conversion was...

The inference time of the model pre- and post-conversion was...

## Assess Model Use Cases

Some of the potential use cases of the people counter app are...

Each of these use cases would be useful because...

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
