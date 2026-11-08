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
    """Organiza a exibição de mídias com controle de tamanho e posição."""
    st.header("📺 Galeria de Mídia")
    
    tab_img, tab_audio, tab_video = st.tabs(["🖼️ Imagens", "🎧 Áudio", "🎥 Vídeos"])
    
    with tab_img:
        st.subheader("Controle de Dimensionamento de Imagem")
        st.write("**Largura Fixa (200px):**")
        st.image("01.jpg", width=200)
        
        st.divider()
        st.write("**Centralizada (via colunas):**")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image("01.jpg", use_container_width=True)

    with tab_audio:
        st.subheader("Player de Áudio")
        # Nota: st.audio não aceita 'width'. Usamos colunas para limitar o tamanho.
        c1, c2 = st.columns([1, 2]) 
        with c1:
            st.audio("house_lo.mp3")

    with tab_video:
        st.subheader("Vídeos com Tamanhos Definidos (Um abaixo do outro)")

        # VÍDEO 1 - GRANDE (Usando proporção de colunas para simular largura)
        st.write("#### 1. Vídeo Formato Grande (Largura: 80%)")
        v_col1_a, v_col1_b, v_col1_c = st.columns([0.1, 0.8, 0.1])
        with v_col1_b:
            st.video("Gameplay.mp4")
            st.caption("Gameplay - Proporção mantida automaticamente")
        
        st.divider()

        # VÍDEO 2 - PEQUENO (Usando colunas para limitar a largura)
        st.write("#### 2. Vídeo Formato Pequeno (Largura: 40%)")
        v_col2_a, v_col2_b, v_col2_c = st.columns([1, 1.5, 1])
        with v_col2_b:
            # Dica de Instrutor: Para forçar altura, seria necessário HTML/CSS. 
            # No Streamlit puro, controlamos a largura e a altura segue a proporção.
            st.video("treiler.mp4")
            st.caption("Trailer - Centralizado e Reduzido")

        # EXEMPLO AVANÇADO: Forçando Altura e Largura via CSS (Opcional para mostrar aos alunos)
        st.divider()
        st.write("#### 3. Vídeo com Tamanho Fixo (Hack via CSS Container)")
        
        # Este CSS força qualquer vídeo dentro deste container a ter um tamanho fixo
        largura_fixa = 400
        altura_fixa = 250
        
        st.markdown(f"""
            <style>
            .video-container iframe, .video-container video {{
                width: {largura_fixa}px !important;
                height: {altura_fixa}px !important;
            }}
            </style>
            <div class="video-container">
            """, unsafe_allow_html=True)
        
        st.video("treiler.mp4") # Este vídeo será afetado pelo CSS acima
        st.markdown("</div>", unsafe_allow_html=True)

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
        st.radio('Escolha seu planeta destino:', ['Marte', 'Vênus', 'Terra'], key="radio_p")

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
    
    st.sidebar.divider()
    escolha = st.sidebar.selectbox("Ir para a seção:", ["Mídias", "Interatividade"])

    if escolha == "Mídias":
        secao_midia()
    else:
        secao_controles()

if __name__ == "__main__":
    main()

