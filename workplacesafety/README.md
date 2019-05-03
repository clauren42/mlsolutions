# Ready 2019 Demo

## Local machine setup

1. Visual Studio Code + Azure ML extension

2. Install required packages for local machine:
    - Automatically via conda:
        - `conda env create -n manufacturing --file env.yml`
        - `conda activate manufacturing`
    - Manually via pip:
        - azureml-sdk
        - numpy
        - Pillow
        - protobuf
        - tensorflow==1.10.0
        - jupyter
        - matplotlib

3. Data files: download from [here](https://contosomanufac0283843562.blob.core.windows.net/demo/data.tar.gz) and extract into the `data`, `images`, and `models` directories.

## Remote setup

1. Ensure you have access to the `scottgu-all-hands` resource group.

## Scenario notes

### Background

Contoso Manufacturing is committed to providing a safe workplace environment for its employees. As part of that goal, they recognize safety equipment - like hard hats and high viz jackets - helps reduce and/or mitigate the risk of injuries on the factory floor. While most of their employees wear the required equipment, adoption is less than 100%, often due to new staff and visitors, and hard to monitor.

To address these challenges, Contoso has decided to use machine learing to automatically identify safety violations in their most high risk areas. By taking an existing object detection model and using transfer learning, they're able to add their own data and quickly develop a custom model with Azure ML.

### Train

It's easy to train any kind of machine learning model with Azure ML, including common frameworks like PyTorch and TensorFlow. In this demo, we'll use a real out-of-the-box TensorFlow object detection sample to build our hazard model.

Train in VS Code (step through `train/run.py`):

* Connect to the workspace
* Provision a GPU cluster (which will already exist)
* Upload data to the datastore (which will already be present)
* Create an experiment (which will already exist)
* Configure the experiment (this actually uses a custom Docker image so optionally talk to that) 
* Submit the experiment using a TensorFlow estimator

### Deploy

Once our model is built and validated, we can easily take it and turn it into a web service and deploy it to AKS for inferencing.

Deploy to AKS (step through `score/run.py`):

* Register the model
* Create an AKS cluster (which will already exist)
* Create a container image (and optionally talk to the score.py file)
* Deploy the service
* Test the service by submitting the factory floor image from the presentation and seeing the results

So we've gone from nothing to a deployed web service in just minutes and all from within Visual Studio Code. Let's take a look at what we've accomplished in the Azure Portal and see how it enable us to collaborate with the rest of our team.

Monitor in Azure:

* Step through Experiments (drill into a recent run to see the loss vs. iteration graph that's driven by adding logging code to TF)
* Continue through Models, Images, Deployments

### Edge

While AKS & Kubernetes are the right choice for general purpose hosting, it might be better in some situations to run your model on an IoT device. These single purpose devices can include cameras and hardware support for model evaluation, making them ideal for onsite and near real-time inferencing. Fortunately, taking the model we've already built and pushing to an IoT Edge device is easy.

Deploy to Edge (step through `score-edge/run.py`):

* Create Edge-specific container image 
* Switch to Azure portal and step through the IoT Edge module provisioning flow
    * Specify the image name (e.g. `contosomanufac5523805767.azurecr.io/contosoimage-edge:1`)
    * While the Qualcomm camera could be used as a prop, the demo is not designed to include deploying to this device
    * The device is not connect so the change can be committed

An alternative flow in this section would be to skip the Edge `run.py` and, instead of building a container, deploy the ML model directly from IoT Edge.