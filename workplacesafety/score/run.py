#%%
import os
os.chdir('./score')

#%%
# Configure workspace
from azureml.core import Workspace

ws = Workspace.from_config()
print(ws.name, ws.resource_group, ws.location, ws.subscription_id, sep = '\n')

#%%
# Prepare model
from azureml.core.model import Model
from azureml.core.run import Run

# register the model for deployment
model = Model.register(model_path = "../models/frozen_inference_graph.pb",
                       model_name = "frozen_inference_graph.pb",
                       description = "Contoso Manufacturing model",
                       workspace = ws)

#%%
# Create an AKS cluster
from azureml.core.compute import AksCompute, ComputeTarget
aks_cluster_name = 'contoso-aks'

# Use the default configuration (can also provide parameters to customize)
prov_config = AksCompute.provisioning_configuration(location='eastus2')

# Create the cluster
aks_target = ComputeTarget.create(workspace=ws, 
                                  name=aks_cluster_name, 
                                  provisioning_configuration=prov_config)

aks_target.wait_for_completion(True)

#%%
# Create a container image
from azureml.core.model import Model
from azureml.core.image import ContainerImage

model = Model.list(ws, name='frozen_inference_graph.pb')[0]

image_config = ContainerImage.image_configuration(execution_script='score.py',
                                                  runtime='python',
                                                  conda_file='score.yml',
                                                  description='Object detection model')

image = ContainerImage.create(name='contosoimage',
                              models=[model],
                              image_config=image_config,
                              workspace=ws)

image

#%%
image.wait_for_creation(show_output = True)

#%%
# Deploy the model as a service
from azureml.core.webservice import Webservice, AksWebservice

image = next((x for x in ContainerImage.list(ws, image_name='contosoimage') if x.creation_state == 'Succeeded'), None)

aks_service_name = 'contosoman'
aks_config = AksWebservice.deploy_configuration(collect_model_data=True, enable_app_insights=True)
aks_service = Webservice.deploy_from_image(workspace=ws, 
                                           name=aks_service_name,
                                           image=image,
                                           deployment_config=aks_config,
                                           deployment_target=aks_target)
aks_service

#%%
aks_service.wait_for_deployment(show_output=True)

#%%
# Test the service
import requests
from azureml.core.webservice import Webservice, AksWebservice

image = open('./samples/Before.jpg', 'rb')
input_data = image.read()
image.close()

aks_service_name = 'contosoman2'
aks_service = AksWebservice(workspace=ws, name=aks_service_name)

auth = 'Bearer ' + aks_service.get_keys()[0]
uri = aks_service.scoring_uri

res = requests.post(url=uri,
                    data=input_data,
                    headers={'Authorization': auth, 'Content-Type': 'application/octet-stream'})

results = res.json()

#%%
# Show the results
import utils
import numpy as np

from matplotlib import pyplot as plt
from PIL import Image

image = Image.open('./samples/Before.jpg')
image_np = utils.load_image_into_numpy_array(image)
category_index = utils.create_category_index_from_labelmap('./samples/label_map.pbtxt', use_display_name=True)

utils.visualize_boxes_and_labels_on_image_array(
    image_np,
    np.array(results['detection_boxes']),
    np.array(results['detection_classes']),
    np.array(results['detection_scores']),
    category_index,
    instance_masks=results.get('detection_masks'),
    use_normalized_coordinates=True,
    line_thickness=8)

plt.figure(figsize=(24, 16))
plt.imshow(image_np)

#%%
os.chdir('..')