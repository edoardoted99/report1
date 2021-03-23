from io import BytesIO

import requests
import pandas as pd

r = requests.get('https://docs.google.com/spreadsheets/d/1Fwj_rBZnBSzBM4HFbi2fyuM0OaWPfAP0gAwCCfVatR8/edit?usp=sharing')
data = r.content
df = pd.read_csv(BytesIO(data), index_col=0)
print(df.head())