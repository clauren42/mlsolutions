# Module_3_Intro to NNs for TS Forecasting

## Useful Resources
* Azure Notebooks: https://aka.ms/AzureNB
* Python Microsoft: https://aka.ms/PythonMS
* Automated Machine Learning Documentation: https://aka.ms/AutomatedMLDocs 
* What is Automated Machine Learning? https://aka.ms/AutomatedML
* Azure Machine Learning Service: https://aka.ms/AzureMLService 
* Azure Data Science Virtual Machine: https://aka.ms/AzureDSVM


## Recurrent Neural Networks for Time Series Forecasting
A collection of examples for using RNNs for time series forecasting with Keras. The original GithHub repo is here: https://github.com/Azure/RNNForTimeSeriesForecasting

The examples include:

- **0_data_setup.ipynb** - set up data that are needed for the experiments
- **1_time_series_arima.ipynb** - ARIMA model for time series forecasting
- **2_one_step_FF_univariate.ipynb** - feed forward neural network model that predicts one step ahead with univariate time series
- **3_one_step_RNN_univariate.ipynb** - recurrent neural network model that predicts one step ahead with univariate time series
- **4_multi_step_RNN_vector_output.ipynb** - recurrent neural network model that outputs a vector of predictions to forecast multiple steps ahead
- **5_multi_step_RNN_encoder_decoder_simple.ipynb** - a simple recurrent neural network encoder-decoder approach to multi-step forecasting

We will be using data from the GEFCom2014 energy forecasting competition. You can download the data from https://www.dropbox.com/s/pqenrr2mcvl0hk9/GEFCom2014.zip?dl=0 and save it in the data folder. 
For more information, please refer to: Tao Hong, Pierre Pinson, Shu Fan, Hamidreza Zareipour, Alberto Troccoli and Rob J. Hyndman, "Probabilistic energy forecasting: Global Energy Forecasting Competition 2014 and beyond", International Journal of Forecasting, vol.32, no.3, pp 896-913, July-September, 2016.