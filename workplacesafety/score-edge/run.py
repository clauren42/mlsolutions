#%%
import os
os.chdir('./score-edge/src')

#%%
# Configure workspace
from azureml.core import Workspace

ws = Workspace.from_config()
print(ws.name, ws.resource_group, ws.location, ws.subscription_id, sep = '\n')

#%%
# Fetch model reference
from azureml.core.model import Model

model = Model.list(ws, name='frozen_inference_graph.pb')[0]

#%%
# Build container image
from azureml.core.image import Image
from azureml.contrib.iot import IotContainerImage

image_config = IotContainerImage.image_configuration(
                                 architecture='arm32v7',
                                 execution_script='main.py',
                                 dependencies=['camera.py','iot.py','ipcprovider.py','utility.py','frame_iterators.py'],
                                 docker_file='Dockerfile',
                                 description='Object detection model (Edge)')

image = Image.create(name = 'contosoimage-edge',
                     models = [model],
                     image_config = image_config, 
                     workspace = ws)
image

#%%
image.wait_for_creation(show_output = True)

#%%
os.chdir('../..')