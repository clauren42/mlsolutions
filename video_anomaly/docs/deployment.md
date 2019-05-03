# Deployment to ACI webserver

So far we have used this approach to process data locally, but you could imagine a scenario where you have a camera to record the video, and you want to process the video in real-time via a webservice. 

This can be done with the following steps. 

1. Create a scoring script
2. Create a docker image
3. Deploy the docker image as a webservice
4. Test the webservice

The webservice *expects* video data inform of a numpy array (n_frames, heigh, width, depth). This array needs to be converted to a list and then into byte encoded json format.

The webservice *returns* the mean squared error of the model's predictions of each video frames.


## Create scoring script

We have created a scoring script for you: `score.py`.  Let's take a look at what it does.  

The scoring script is the script that is run when the webservice is deployed and also everytime data is sent to the webservice for processing.

Apart from importing the modules needed for processing data and creating the network model, you will find two methods:

1. init - which is executed only once, when the webservice is started.
2. run - which is executed everytime data is sent to the webservice for processing.


## Create a docker image

Filename: `created_docker_iamge.py`

We use the above scoring script, define dependencies for a conda environmnet in which to execute the scoring script, and also include all custom scripts needed by the scoring script.


## Deploy the docker image as a webservice

Filename: `deploy_aci.py`

## Test the webservice

Use the script `test_aci.py` to see whether you webservices behaves as expected.
