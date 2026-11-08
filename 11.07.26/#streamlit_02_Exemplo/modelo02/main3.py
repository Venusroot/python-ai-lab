import streamlit as st

def configurar_pagina():
    """Configura o layout e título da página."""
    st.set_page_config(
        page_title="App do Instrutor - Aula de Layout", 
        layout="wide", 
        initial_sidebar_state="expanded"
    )
    st.title("🚀 Demonstração Profissional: Mídias e Interatividade")
    st.markdown("---")

def secao_midia():
    """Organiza a exibição de mídias com diferentes configurações de tamanho."""
    st.header("📺 Galeria de Mídia")
    
    tab_img, tab_audio, tab_video = st.tabs(["🖼️ Imagens (Tamanhos)", "🎧 Áudio", "🎥 Vídeos"])
    
    with tab_img:
        st.subheader("Controle de Dimensionamento de Imagem")
        
        # Exemplo 1: Largura Fixa em Pixels (Bom para ícones ou logos)
        st.write("**1. Largura Fixa (200px):**")
        st.image("01.jpg", caption="Tamanho fixo pequeno", width=200)
        
        st.divider() # Linha divisória para organizar

        # Exemplo 2: Usando Colunas para centralizar e limitar o tamanho (Design Profissional)
        st.write("**2. Centralizada e limitada por colunas (Ocupando 50% do centro):**")
        col1, col2, col3 = st.columns([1, 2, 1]) # Proporção: a do meio é o dobro das laterais
        with col2:
            st.image("01.jpg", caption="Imagem centralizada", use_container_width=True)

        st.divider()

        # Exemplo 3: Responsiva (Ocupa toda a largura disponível)
        st.write("**3. Responsiva (Ocupando 100% da largura da página):**")
        st.image("01.jpg", caption="Imagem em tela cheia", use_container_width=True)

    with tab_audio:
        st.subheader("Player de Áudio")
        st.audio("house_lo.mp3",width=200)

    with tab_video:
        st.write("Vídeos organizados lado a lado:")
        col_v1, col_v2 = st.columns(2)
        with col_v1:
            st.video("Gameplay.mp4")
            st.caption("Gameplay.mp4")
        with col_v2:
            st.video("treiler.mp4")
            st.caption("treiler.mp4")

def secao_controles():
    """Centraliza os componentes de input e lógica de interação."""
    st.header("🎮 Controles e Interação")

    col_esq, col_dir = st.columns(2)

    with col_esq:
        st.subheader("Seleções Simples")
        aceito = st.checkbox("Eu aceito os termos")
        if st.button('Clique aqui para Processar'):
            if aceito:
                st.success("✅ Processado com sucesso!")
            else:
                st.warning("⚠️ Você precisa aceitar os termos primeiro.")

        planeta_radio = st.radio('Escolha seu planeta destino:', ['Marte', 'Vênus', 'Terra'], key="radio_p")

    with col_dir:
        st.subheader("Seleções Avançadas")
        st.selectbox('Selecione para Observação:', ['Júpiter', 'Netuno', 'Marte'])
        st.multiselect('Planetas para Visitação:', ['Terra', 'Saturno', 'Netuno'])
        st.select_slider('Nível de Exploração:', ['Marte', 'Netuno', 'Terra'])

def secao_perfil():
    """Lógica condicional na barra lateral."""
    st.sidebar.header("👤 Perfil do Usuário")
    genero = st.sidebar.radio('Escolha o gênero:', ['Masculino', 'Feminino', 'Outro'])
    
    if genero == 'Masculino':
        st.sidebar.write("Você selecionou: **Masculino**")
    elif genero == 'Feminino':
        st.sidebar.write("Você selecionou: **Feminino**")
    else:
        st.sidebar.write("Você selecionou: **Outro**")

def main():
    """Função principal que coordena o app."""
    configurar_pagina()
    secao_perfil()
    
    # Menu de navegação na barra lateral
    st.sidebar.divider()
    escolha = st.sidebar.selectbox("Ir para a seção:", ["Mídias", "Interatividade"])

    if escolha == "Mídias":
        secao_midia()
    else:
        secao_controles()

if __name__ == "__main__":
    main()
