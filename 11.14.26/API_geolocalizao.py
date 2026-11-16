
import streamlit as st
import requests

# =====================================
# CONFIGURAÇÃO
# =====================================

st.set_page_config(
    page_title="Localiza+ | Geolocalização",
    page_icon="📍",
    layout="centered"
)

# =====================================
# CSS
# =====================================

st.markdown("""
<style>
.stApp {
    background-color: #FFFFFF;
}

h1, h2, h3, h4 {
    color: #292929 !important;
}

p, label {
    color: #555555 !important;
}

.stButton > button {
    background-color: #E98243;
    color: white;
    border: none;
    border-radius: 8px;
    height: 45px;
    font-weight: 600;
    width: 100%;
}

.stButton > button:hover {
    background-color: #D96F30;
    color: white;
}

.resultado {
    background-color: #FFF8F2;
    padding: 18px;
    border-radius: 10px;
    border: 1px solid #F5E2D3;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)


# =====================================
# FUNÇÃO: BUSCAR COORDENADAS
# =====================================

def buscar_coordenadas(cidade):

    url = "https://geocoding-api.open-meteo.com/v1/search"

    parametros = {
        "name": cidade,
        "count": 10,
        "language": "pt",
        "format": "json"
    }

    resposta = requests.get(
        url,
        params=parametros,
        timeout=10
    )

    resposta.raise_for_status()

    dados = resposta.json()

    return dados.get("results", [])


# =====================================
# INTERFACE
# =====================================

st.title("📍 Localiza+")

st.caption(
    "Sistema de consulta de localização geográfica."
)

st.divider()

st.subheader("Consulta de geolocalização")

cidade = st.text_input(
    "Digite o nome da cidade",
    placeholder="Exemplo: São Paulo"
)

if st.button("Buscar localização"):

    if not cidade.strip():

        st.warning("Digite o nome de uma cidade.")

    else:

        try:

            with st.spinner("Buscando localização..."):

                resultados = buscar_coordenadas(cidade.strip())

            if not resultados:

                st.warning("Nenhuma cidade encontrada.")

            else:

                st.success("Localização encontrada!")

                # SELEÇÃO DE CIDADES

                opcoes = [
                    f"{r.get('name', 'Não informado')} - "
                    f"{r.get('admin1', 'Estado não informado')} - "
                    f"{r.get('country', 'País não informado')}"
                    for r in resultados
                ]

                indice = st.selectbox(
                    "Selecione a cidade desejada",
                    range(len(opcoes)),
                    format_func=lambda i: opcoes[i]
                )

                local = resultados[indice]

                st.divider()

                st.subheader("Informações geográficas")

                col1, col2 = st.columns(2)

                with col1:

                    st.markdown(
                        f"""
                        <div class="resultado">
                            <small>Latitude</small>
                            <h3>{local['latitude']}</h3>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                with col2:

                    st.markdown(
                        f"""
                        <div class="resultado">
                            <small>Longitude</small>
                            <h3>{local['longitude']}</h3>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                st.write(
                    "**Cidade:**",
                    local.get("name", "Não informado")
                )

                st.write(
                    "**Estado/Região:**",
                    local.get("admin1", "Não informado")
                )

                st.write(
                    "**País:**",
                    local.get("country", "Não informado")
                )

                st.write(
                    "**Código do país:**",
                    local.get("country_code", "Não informado")
                )

                st.divider()

                st.subheader("Mapa da localização")

                st.map({
                    "latitude": [local["latitude"]],
                    "longitude": [local["longitude"]]
                })

        except requests.exceptions.Timeout:

            st.error("Tempo limite de conexão excedido.")

        except requests.exceptions.RequestException:

            st.error("Erro ao conectar com a API.")

        except (KeyError, ValueError):

            st.error("Erro ao interpretar os dados recebidos.")

# =====================================
# RODAPÉ
# =====================================

st.divider()

st.caption("Localiza+ | Geolocalização com Open-Meteo")
