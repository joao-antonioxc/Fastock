import json

import pandas as pd
import requests


df = pd.read_csv('veiculos.csv', sep=';')

marcas = set (df['marca'])

# print(marcas)

carros = {}

for marca in marcas:
    carros[marca] = []

dfDict = df.to_dict('index')

for veiculo in dfDict:
    carros[dfDict[veiculo]['marca']].append(dfDict[veiculo]['carro'])

# print(df.to_json())
# print(carros)

link_db = 'https://fastok-db-default-rtdb.firebaseio.com/'

# req_post = requests.post(f'{link_db}/veiculos/{marcas}/.json', data=df.to_json(orient='records'))
# req_post = requests.Request(f'{link_db}/.json', data=json.dumps(carros), method="PATCH")
req_post = requests.patch(f'{link_db}/veiculos/.json', data=json.dumps(carros))
