from azureml.core.runconfig import AzureContainerRegistry, DockerEnvironment, EnvironmentDefinition, PythonEnvironment
registry = AzureContainerRegistry()
registry.address = 'contosomanufac5523805767.azurecr.io'
registry.username = 'contosomanufac5523805767'
registry.password = 'RC+cx6OiEhgK8MY1rSGkkaj8eYnGncNC'

docker_config = DockerEnvironment()
docker_config.enabled = True
docker_config.base_image = 'contosoml/base-gpu:0.2.1'
docker_config.base_image_registry = registry
docker_config.gpu_support = True

python_config = PythonEnvironment()
python_config.user_managed_dependencies = True
