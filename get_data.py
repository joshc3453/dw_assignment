import pandas as pd
from sodapy import Socrata
import config_file

data_url = 'healthdata.gov'
data_set = 'j8mb-icvb'
app_token = config_file.app_token

client = Socrata(data_url, config_file.app_token) 

client.timeout = 60

results = client.get(data_set, limit=200000)

df = pd.DataFrame.from_records(results)

df.to_csv('dataset.csv', index=False)