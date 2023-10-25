import pandas as pd
import numpy as np

df = pd.read_excel('consolidado_por_uf.xlsx', sheet_name='consolidado_por_uf')

colunaQTD = df['Quantidade de Matrículas'].tolist()
colunaDA = df['Dependência Administrativa'].tolist()


dependencias = {
}

for c in range(len(colunaDA)):
    if not colunaDA[c] in dependencias:
        dependencias[colunaDA[c]] = colunaQTD[c]
    else:
        dependencias[colunaDA[c]] += colunaQTD[c]
        
print(dependencias)