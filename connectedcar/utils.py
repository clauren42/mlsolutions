
from adal import AuthenticationContext
import requests
import pandas as pd
from datetime import datetime
from io import StringIO, BytesIO

def read_stream_from_adls(endpoint, auth):
    headers = {"Authorization": "Bearer " + auth['accessToken']}
    return requests.get(endpoint, data = None, headers = headers, stream=True)

def read_from_adls(endpoint, auth):
    headers = {"Authorization": "Bearer " + auth['accessToken']}
    return requests.get(endpoint, data = None, headers = headers)

# generate AAD token for REST API authentication
def generate_aad_token():
    resource = "https://storage.azure.com/"
    client_secret = "Lky5pTg2teniHdbeTlmOuivjdIPBPcwMQJ49wGwKiXA="
    client_id = "bd8e91da-c58c-4407-95e0-a8ecad012fc7"
    authority_url = "https://login.microsoftonline.com/72f988bf-86f1-41af-91ab-2d7cd011db47/"
    auth_context = AuthenticationContext(authority_url, api_version = None)
    return auth_context.acquire_token_with_client_credentials(resource, client_id, client_secret)

def type_conveter(input_type):
    switcher = {
        'boolean': 'bool',
        'int64': 'int64',
        'decimal': 'float64'
    }
    return switcher.get(input_type, 'str')

def read_from_adls_with_cdm_format(entity, schema = "cdm"):
    auth = generate_aad_token()
    csv_path = entity.partitions[0].location
    csv_bytes = read_stream_from_adls(endpoint = csv_path, auth = auth).content
    # read to pandas dataframe with defined schema from model.json
    names = [attribute.name for attribute in entity.attributes]
    types = dict([(attribute.name, type_conveter(attribute.dataType.value)) for attribute in entity.attributes]) if schema is "cdm" else dict([(attribute.name, 'str') for attribute in entity.attributes])
    buff = BytesIO(csv_bytes)
    df = pd.read_csv(buff, names=names, dtype=types, header=None)
    buff.close()
    return df
