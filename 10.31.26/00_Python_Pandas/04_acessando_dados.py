import pandas as pd

try:
    df_vendas = pd.read_csv("00_Python_Pandas/vendas.csv")
    print(df_vendas)

except FileNotFoundError:
    print("Erro: o arquivo 'vendas.csv' não foi encontrado.")