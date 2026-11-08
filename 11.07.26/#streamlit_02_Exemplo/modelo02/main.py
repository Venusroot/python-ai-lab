import streamlit as st

st.subheader("Imagem :") # Cria um título de nível secundário
st.image("01.jpg")       # Carrega e exibe na tela o arquivo de imagem 

st.subheader("Audio :")  #  Cria um subcabeçalho para a seção de áudio.
st.audio("house_lo.mp3") #  Exibe um player de áudio para reproduzir 

st.subheader("Video :")  # Cria um subcabeçalho para a seção de vídeo.
st.video("Gameplay.mp4") # Exibe um player de vídeo para reproduzir o arquivo Gameplay.mp4.


st.subheader("Video :")  # Cria um subcabeçalho para a seção de vídeo.
st.video("treiler.mp4") # Exibe um player de vídeo para reproduzir o arquivo treiler.mp4.

# =================================================

#  Cria uma caixa de seleção (checkbox) com o rótulo "yes". 
st.checkbox("yes") 
#  Cria um botão com o texto 'click'
st.button('click') 
# Cria botões de opção redondos onde o usuário só pode escolher uma opção entre as listadas
st.radio('Escolha seu planeta', ['Marte', 'Venus','Terra']) 
# Cria um menu suspenso (dropdown) para escolher uma opção.
st.selectbox('Escolha seu planeta', ['Jupiter', 'Netuno','Marte']) 
# Cria um campo onde o usuário pode selecionar várias opções ao mesmo tempo da lista fornecida
st.multiselect('Escolha seu planeta', ['Terra', 'Saturno','Netuno']) 
# Cria uma barra deslizante (slider) que permite ao usuário escolher entre opções específicas
st.select_slider('Escolha seu planeta', ['Marte', 'Netuno','Terra']) 

# ==================================================

genero = st.radio('Escolha o gênero', ['Masculino', 'Feminino'])
if genero == 'Masculino':
    st.write("Você selecionou Masculino")
else:
    st.write("Você selecionou Feminino")