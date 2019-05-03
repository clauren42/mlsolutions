# Introduction to Azure Machine Learning service

This module contains a subset of example notebooks demonstrating the [Azure Machine Learning](https://azure.microsoft.com/en-us/services/machine-learning-service/) Python SDK which allows you to build, train, deploy and manage machine learning solutions using Azure. The AML SDK allows you the choice of using local or cloud compute resources, while managing and maintaining the complete data science workflow from the cloud.

![Azure ML workflow](https://raw.githubusercontent.com/MicrosoftDocs/azure-docs/master/articles/machine-learning/service/media/overview-what-is-azure-ml/aml.png)

## Quick installation
```sh
pip install azureml-sdk
pip install azureml-dataprep
```
Read more detailed instructions on [how to set up your environment](./NBSETUP.md) using Azure Notebook service, your own Jupyter notebook server, or Docker.

## How to navigate and use the example notebooks?
You should always run the [Configuration](./configuration.ipynb) notebook first when setting up a notebook library on a new machine or in a new environment. It configures your notebook library to connect to an Azure Machine Learning workspace, and sets up your workspace and compute to be used by many of the other examples. 

Start with [01. Run Experiment](./01.run-experiment.ipynb) and [02. Deploy Web Service](./02.deploy-web-service.ipynb) to get familiar with Azure Machine Learning's core concepts: {workspaces, experiments, and runs}; and {models, images, and services}, respectively.

Then, explore [Azure Machine Learning's Data Prep SDK](./5min-dataprep-intro.ipynb) in a quick 5-min walkthrough. The Data Prep SDK is a little unique in that it does not require Azure Machine Learning resources to get started; you can use it to prepare any data you like independent of Azure Machine Learning services. However, we'll later show how you can use it to feed into your Azure Machine Learning Automated ML flows.

If you want to...

 * ...try out and explore Azure ML, start with image classification tutorials: [Part 1 (Training)](./tutorials/img-classification-part1-training.ipynb) and [Part 2 (Deployment)](./tutorials/img-classification-part2-deploy.ipynb).
 * ...prepare your data and do automated machine learning, start with regression tutorials: [Part 1 (Data Prep)](./tutorials/regression-part1-data-prep.ipynb) and [Part 2 (Automated ML)](./tutorials/regression-part2-automated-ml.ipynb).
 * ...learn more about how to use other Azure ML services like model deployment, hyperparameter tuning, and model monitoring, *visit our [Azure ML notebooks repo](https://github.com/Azure/MachineLearningNotebooks).*

---
## Documentation

 * Quickstarts, end-to-end tutorials, and how-tos on the [official documentation site for Azure Machine Learning service](https://docs.microsoft.com/en-us/azure/machine-learning/service/).
 * [Python SDK reference](https://docs.microsoft.com/en-us/python/api/overview/azure/ml/intro?view=azure-ml-py)
 * Azure ML Data Prep SDK [overview](https://aka.ms/data-prep-sdk), [Python SDK reference](https://aka.ms/aml-data-prep-apiref), and [tutorials and how-tos](https://aka.ms/aml-data-prep-notebooks).
