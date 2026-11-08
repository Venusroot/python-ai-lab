import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.markdown("# Minha Pagina 2 - texto corpo")

st.sidebar.markdown("Meu site 02 - texto menu")

st.header("Hello Python !!")

opcao = st.selectbox(
    'Esolha um Departamento:',
    ['RH', 'T.I', 'Vendas', 'Marketing']
)
st.write(f'Departamento Selecionado: {opcao}')



