import pandas as pd

# CRIA UMA DATAFRAME JUNTANDO SERIES
def criar_dataframe_juntando_series(valor1, valor2):
    return pd.concat([valor1, valor2], axis=1) 

