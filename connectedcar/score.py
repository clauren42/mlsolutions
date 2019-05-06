import pickle
import json
import numpy
import azureml.train.automl
from sklearn.externals import joblib
from azureml.core.model import Model

def init():
    global model
    model_path = Model.get_model_path('model.pkl') # this name is model.id of model that we want to deploy
    # deserialize the model file back into a sklearn model
    model = joblib.load(model_path)

# [bulk] def run(rawdata):
def run(**kwargs):
    try:
        # for bulk services
        #data = json.loads(rawdata)['data']
        #data = numpy.array(data)
        
        # for single record services
        data = numpy.array([numpy.array(list(kwargs.values()))])
        result = model.predict(data)
    except Exception as e:
        result = str(e)
        return {"error": result}
    # [bulk] return {"result": result.tolist()}
    return {"result": result[0]}
