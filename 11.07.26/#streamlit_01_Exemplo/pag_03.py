import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# =====================================================
# edicao de tabelas usando Pandas
data = {
    'Nome':['Ana', 'Bruno', 'João'],
    'Idade':[23, 25, 28],
    'Salario':[5000, 3500, 2800]
}

df = pd.DataFrame(data)
st.dataframe(df) # tabela interativa
st.table(df) # tabela simplificada


# ==========================
# edicao grafico em matplotlib
fig, ax = plt.subplots()
ax.bar(df['Nome'], df['Salario'])
st.pyplot(fig)


idade = st.slider('Selecione sua idade' , 0, 100, 20)
st.write(f'Idade Selecionada: {idade}')


# ===========================
col1, col2 = st.columns(2)

with col1:
    st.header('Coluna 01 - Texto')
    st.write('Conteudo coluna 1')

with col2:
    st.header('Coluna 02 - Texto')
    st.write('Conteudo coluna 2')

# =================================
# Criando um DataFrame
data = {'Nome': ['Alice', 'Bob', 'Charlie'], 'Idade': [24, 27, 22], 'Seleção':[True, False, True]}
df = pd.DataFrame(data)

# Exibindo a tabela editável
edited_df = st.data_editor(df)

