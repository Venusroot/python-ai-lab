import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.markdown("# Minha Pagina 1 - texto corpo")

st.sidebar.markdown("Meu site 01 - texto menu")

# -------------------------------
# edicao de tabelas usando Pandas
data = {
    'Nome':['João', 'Pedro', 'Tiago', 'Alicia'],
    'Idade':[16, 15, 22, 18],
    'Salario':[5000, 4500, 6000, 5800],
    'Altura':[1.70, 1.65, 1.80, 1.75]
}

df = pd.DataFrame(data)
st.dataframe(df) # tabela interativa
st.table(df)  #tabela simplificada




