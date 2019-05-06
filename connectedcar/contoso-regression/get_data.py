import pandas as pd
import numpy as np
import CdmModel
from utils import read_from_adls_with_cdm_format, read_from_adls, generate_aad_token

model_url = "https://contosoautodatalake.dfs.core.windows.net/powerbi/AIDemos/AMLDataflow/model.json"

def get_data():  
    aad_token = generate_aad_token()
    model_data = read_from_adls(endpoint = model_url,
                                auth = aad_token)
    model = CdmModel.Model.fromJson(model_data.json())

    train_data = read_from_adls_with_cdm_format(model.entities[0])
    
    X = train_data.iloc[:,1:73]
    Y = train_data.iloc[:,0].values

    return { "X" : X.as_matrix(), "y" : Y.flatten() }
