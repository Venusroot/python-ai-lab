import streamlit as st

def configurar_pagina():
    """Configura o layout e título da página."""
    st.set_page_config(page_title="App do Instrutor", layout="wide")
    st.title("🚀 Demonstração de Componentes Streamlit")

def secao_midia():
    """Organiza a exibição de arquivos multimídia em abas."""
    st.header("📺 Galeria de Mídia")
    
    # Uso de abas para economizar espaço vertical
    tab_img, tab_audio, tab_video = st.tabs(["Imagens", "Áudio", "Vídeos"])
    
    with tab_img:
        st.subheader("Visualização de Imagem")
        st.image("01.jpg", caption="Legenda da Imagem", use_container_width=True)

    with tab_audio:
        st.subheader("Player de Áudio")
        st.audio("house_lo.mp3")

    with tab_video:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Gameplay")
            st.video("Gameplay.mp4")
        with col2:
            st.subheader("Trailer")
            st.video("treiler.mp4")

def secao_controles():
    """Centraliza os componentes de input e lógica de interação."""
    st.header("🎮 Controles e Interação")

    # Colunas para organizar os widgets de seleção
    col_esq, col_dir = st.columns(2)

    with col_esq:
        aceito = st.checkbox("Eu aceito os termos")
        if st.button('Clique aqui para Processar'):
            if aceito:
                st.success("Processado com sucesso!")
            else:
                st.warning("Você precisa aceitar os termos primeiro.")

        planeta_radio = st.radio('Escolha seu planeta destino:', ['Marte', 'Vênus', 'Terra'], key="radio_p")
        st.info(f"Destino via Radio: {planeta_radio}")

    with col_dir:
        planeta_select = st.selectbox('Selecione para Observação:', ['Júpiter', 'Netuno', 'Marte'])
        planetas_multi = st.multiselect('Planetas para Visitação:', ['Terra', 'Saturno', 'Netuno'])
        planeta_slider = st.select_slider('Nível de Exploração:', ['Marte', 'Netuno', 'Terra'])

def secao_perfil():
    """Exemplo de lógica condicional simples na barra lateral."""
    st.sidebar.header("Perfil do Usuário")
    genero = st.sidebar.radio('Escolha o gênero', ['Masculino', 'Feminino', 'Outro'])
    
    if genero == 'Masculino':
        st.sidebar.write("👤 Usuário selecionou Masculino")
    elif genero == 'Feminino':
        st.sidebar.write("👩 Usuária selecionou Feminino")
    else:
        st.sidebar.write("🌈 Usuário selecionou Outro")

def main():
    """Função principal que coordena o app."""
    configurar_pagina()
    secao_perfil()
    
    # Criando um menu de navegação simples
    menu = ["Mídias", "Interatividade"]
    escolha = st.sidebar.selectbox("Navegar para:", menu)

    if escolha == "Mídias":
        secao_midia()
    else:
        secao_controles()

if __name__ == "__main__":
    main()
