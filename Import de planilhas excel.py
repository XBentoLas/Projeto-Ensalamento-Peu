import pandas as pd
import json

df = pd.read_excel('salas.xlsx')

salas_json = df.to_dict(orient='records')

print(salas_json)

with open('salas.json', 'w') as f:
    json.dump(salas_json, f, indent=4)