# Forecasting financial time series with deep learning on Azure
https://conferences.oreilly.com/artificial-intelligence/ai-ny/public/schedule/detail/73899


## Useful Resources
* Azure Notebooks: https://aka.ms/AzureNB
* Azure Machine Learning Service: https://aka.ms/AzureMLService 
	* Data Prep:
		* What is Data Prep? http://aka.ms/AzureMLDataPrep (video)
		* Data Prep documentation: http://aka.ms/AzureMLDataPrepNB 
	* Automated ML:
		* What is Automated ML? https://aka.ms/AutomatedML 
		* Automated ML documentation: https://aka.ms/AutomatedMLDocs
* Python Microsoft: https://aka.ms/PythonMS 
* Azure Data Science Virtual Machine: https://aka.ms/AzureDSVM


## Introduction
Time series data is an invaluable source of information used for future strategy and planning operations everywhere from finance to education and healthcare. In the past few decades, machine learning model-based forecasting has also become very popular in the private and the public decision-making process.

In this hands-on course, Francesca Lazzeri walks you through the core steps for building, training, and deploying your time series forecasting models. You'll build a theoretical foundation as you cover the essential aspects of time series representations, modeling, and forecasting before diving into the classical methods for forecasting time series data. Francesca guides you through using some of the more common methods, including simple exponential smoothing, autoregressive integrated moving average (ARIMA), and neural networks for time series forecasting. You'll then gain hands-on experience applying these models to a real-world scenario, using machine learning components available in open source Python packages, such as scikit-learn, Keras, and TensorFlow. With these guidelines in mind, you'll be better equipped to deal with time series in your everyday work.


## Data
The data for this course is from the website Data Market, which provides access to a large number of time series datasets. Specically, the Time Series Data Library (https://datamarket.com/data/list/?q=provider:tsdl) created by Rob Hyndman, Professor of Statistics at Monash University, Australia.

Moreover, we will be using data from the GEFCom2014 energy forecasting competition. You can download the data from [https://www.dropbox.com/s/pqenrr2mcvl0hk9/GEFCom2014.zip?dl=0](https://www.dropbox.com/s/pqenrr2mcvl0hk9/GEFCom2014.zip?dl=0) and save it in the *data* folder. For more information, please refer to: Tao Hong, Pierre Pinson, Shu Fan, Hamidreza Zareipour, Alberto Troccoli and Rob J. Hyndman, "Probabilistic energy forecasting: Global Energy Forecasting Competition 2014 and beyond", International Journal of Forecasting, vol.32, no.3, pp 896-913, July-September, 2016.

Finally, for the stock market predictions use case, we will be using data from Alpha Vantage (you will first need an API key, which you can obtain for free [here](https://www.alphavantage.co/support/#api-key)) and from [Kaggle] (https://www.kaggle.com/borismarjanovic/price-volume-data-for-all-us-stocks-etfs). And for the notebook named "RNN_LSTM_GRU.ipynb", we will be using daily OHLC data for the stock of “RELIANCE” trading on National Stock Exchange for the time period from 1st January 1996 to 30 Sep 2018. 

## Prerequisites
- Experience coding in Python
- A basic understanding of machine learning and deep learning topics and terminology as well as the mathematics used for machine learning
- A laptop with an up-to-date version of the Edge or Chrome browser and the Azure Machine Learning Python SDK installed
- An Azure Notebooks account

## Azure Notebooks Setup (1 Minute)
Microsoft Azure Notebooks is a free service that provides Jupyter Notebooks in cloud and has a support for R, Python and F#. We will use Microsoft Azure Notebook for this tutorial. Here are quick 3 steps to set it up:

1. Go to Azure Notebook page http://aka.ms/AzureNB and click '***Sign In***' on the top right.
2. Use your Microsoft account to sign in. If you don't have a personal Microsoft account, you can click '***Create one***' with any email address you have for free. (*Note: You can use your personal Microsoft account. If you use your organizational account, you will need to go through the login process by your organization.*)
3. If this is the first time you use Azure Notebook, you will need to create a user ID and click '***Save***'. Now you are all set!
4. For more information, visit: http://aka.ms/AzureNB


## Tutorial Code and Data Setup (5 Minutes)
The following steps will guide you to setup code and data in your Azure Notebook environment for the training.

1. Once you are logged in to Azure Notebooks, on the top right, select '***Clone***' tab. Then type in any name you prefer for '***Project Name***' and '***Project ID***'. Once you have filled in all boxes, click '***Clone***'. Wait till you see a list of files cloned.
2. On the top left, select '***Free Compute***' as compute target option from the dropdown menu.
3. Make sure you see '***Python 3.6***' kernel on the top right for your notebook environment. If not, you can select '***Kernel***', then '***Change kernel***' to make changes.
4. Run each cell in the notebook by click '***Run***' on top. This notebook will download sample data to your environment and visualize the data. Wait and make sure you can see all the visualizations. Now you are all set!