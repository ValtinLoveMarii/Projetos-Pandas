import pandas as pd

# 1. Defina sua função (Correta)
def criar_dataframe_juntando_series(valor1, valor2):
    return pd.concat([valor1, valor2], axis=1) 