# Precisa baixar com o pip install ambos, streamlit e também request 
# Para rodar: streamlit run "E:\SENAI - IAGPT-233\Aulas\11.14.26\API_CEP.py"          
#

import streamlit as st
import requests

# =====================================
# CONFIGURAÇÃO DA PÁGINA
# =====================================

st.set_page_config(
    page_title="Localiza+ | CEP e Clima",
    page_icon="📍",
    layout="centered"
)


# =====================================
# ESTILIZAÇÃO CSS
# =====================================

st.markdown("""
<style>

/* FUNDO PRINCIPAL */
.stApp {
    background-color: #FFFFFF;
}

/* CONTEÚDO PRINCIPAL */
.main .block-container {
    background-color: #FFFFFF;
    padding-top: 2rem;
}

/* TÍTULOS */
h1, h2, h3, h4, h5, h6 {
    color: #292929 !important;
}

/* TEXTOS GERAIS */
p, span, label, li {
    color: #444444;
}

/* TEXTOS DO STREAMLIT */
[data-testid="stMarkdownContainer"] p {
    color: #444444 !important;
}

/* LEGENDAS */
.stCaption, [data-testid="stCaptionContainer"] {
    color: #777777 !important;
}

/* CAMPOS DE TEXTO */
.stTextInput input {
    background-color: #FFFFFF !important;
    color: #292929 !important;
    border: 1px solid #E5D8CF !important;
    border-radius: 8px !important;
}

/* PLACEHOLDER */
.stTextInput input::placeholder {
    color: #999999 !important;
}

/* BOTÕES */
.stButton > button {
    background-color: #E98243 !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 8px !important;
    height: 45px;
    font-weight: 600;
    width: 100%;
}

/* TEXTO DOS BOTÕES */
.stButton > button p {
    color: #FFFFFF !important;
}

/* EFEITO HOVER */
.stButton > button:hover {
    background-color: #D96F30 !important;
    color: #FFFFFF !important;
}

/* RESULTADO DO ENDEREÇO */
.resultado {
    background-color: #FFF8F2;
    padding: 18px;
    border-radius: 10px;
    border: 1px solid #F5E2D3;
    margin-bottom: 10px;
    color: #292929 !important;
}

.resultado small {
    color: #777777 !important;
}

.resultado h4 {
    color: #292929 !important;
}

/* CARD DO CLIMA */
.clima {
    background-color: #FFF8F2;
    padding: 22px;
    border-radius: 12px;
    border: 1px solid #F5E2D3;
    text-align: center;
}

.clima p {
    color: #666666 !important;
}

/* MÉTRICAS */
[data-testid="stMetricValue"] {
    color: #292929 !important;
}

[data-testid="stMetricLabel"] {
    color: #666666 !important;
}

/* DIVISORES */
hr {
    border-color: #EEEEEE !important;
}

</style>
""", unsafe_allow_html=True)



# =====================================
# FUNÇÃO: CONSULTAR CEP
# =====================================

def consultar_cep(cep):

    url = f"https://viacep.com.br/ws/{cep}/json/"

    resposta = requests.get(url, timeout=10)

    resposta.raise_for_status()

    dados = resposta.json()

    if "erro" in dados:
        return None

    return dados


# =====================================
# FUNÇÃO: CONSULTAR COORDENADAS
# =====================================

def consultar_coordenadas(cidade, estado):

    url = "https://geocoding-api.open-meteo.com/v1/search"

    parametros = {
        "name": cidade,
        "count": 10,
        "language": "pt",
        "format": "json",
        "countryCode": "BR"
    }

    resposta = requests.get(
        url,
        params=parametros,
        timeout=10
    )

    resposta.raise_for_status()

    dados = resposta.json()

    locais = dados.get("results", [])

    for local in locais:

        if local.get("admin1", "").lower() == estado.lower():

            return {
                "latitude": local["latitude"],
                "longitude": local["longitude"]
            }

    return None


# =====================================
# FUNÇÃO: CONSULTAR CLIMA
# =====================================

def consultar_clima(latitude, longitude):

    url = "https://api.open-meteo.com/v1/forecast"

    parametros = {
        "latitude": latitude,
        "longitude": longitude,
        "current": (
            "temperature_2m,"
            "relative_humidity_2m,"
            "apparent_temperature,"
            "is_day,"
            "precipitation,"
            "weather_code,"
            "wind_speed_10m"
        ),
        "timezone": "auto"
    }

    resposta = requests.get(
        url,
        params=parametros,
        timeout=10
    )

    resposta.raise_for_status()

    dados = resposta.json()

    return dados["current"]


# =====================================
# INTERFACE PRINCIPAL
# =====================================

st.title("📍 Localiza+")

st.caption(
    "Consulte endereços e condições climáticas "
    "de qualquer região do Brasil."
)

st.divider()

st.subheader("Consulta de endereço")

cep = st.text_input(
    "Digite o CEP",
    placeholder="Exemplo: 01001-000",
    max_chars=9
)

consultar = st.button("Consultar endereço")

if consultar:

    cep = cep.replace("-", "").strip()

    # Validação do CEP

    if len(cep) != 8 or not cep.isdigit():

        st.error("Digite um CEP válido com 8 números.")

    else:

        try:

            with st.spinner("Consultando endereço..."):

                endereco = consultar_cep(cep)

            if endereco is None:

                st.warning("CEP não encontrado.")

            else:

                st.success("Endereço encontrado!")

                # DADOS DO ENDEREÇO

                st.subheader("📍 Informações do endereço")

                col1, col2 = st.columns(2)

                with col1:

                    st.markdown(
                        f"""
                        <div class="resultado">
                            <small>CEP</small>
                            <h4>{endereco.get('cep', 'Não informado')}</h4>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                with col2:

                    st.markdown(
                        f"""
                        <div class="resultado">
                            <small>Estado</small>
                            <h4>{endereco.get('uf', 'Não informado')}</h4>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                st.write(
                    "**Logradouro:**",
                    endereco.get("logradouro") or "Não informado"
                )

                st.write(
                    "**Complemento:**",
                    endereco.get("complemento") or "Não informado"
                )

                st.write(
                    "**Bairro:**",
                    endereco.get("bairro") or "Não informado"
                )

                st.write(
                    "**Cidade:**",
                    endereco.get("localidade") or "Não informado"
                )

                st.write(
                    "**Estado:**",
                    endereco.get("estado") or endereco.get("uf") or "Não informado"
                )

                st.divider()

                # CONSULTA DO CLIMA

                st.subheader("🌤️ Clima da região")

                cidade = endereco.get("localidade")
                estado = endereco.get("uf")

                with st.spinner("Consultando condições climáticas..."):

                    coordenadas = consultar_coordenadas(
                        cidade,
                        estado
                    )

                    if coordenadas:

                        clima = consultar_clima(
                            coordenadas["latitude"],
                            coordenadas["longitude"]
                        )

                        st.markdown(
                            f"""
                            <div class="clima">
                                <h2 style="color:#E98243;">
                                    {clima['temperature_2m']}°C
                                </h2>
                                <p>Temperatura atual</p>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                        col1, col2 = st.columns(2)

                        with col1:

                            st.metric(
                                "Sensação térmica",
                                f"{clima['apparent_temperature']}°C"
                            )

                            st.metric(
                                "Umidade",
                                f"{clima['relative_humidity_2m']}%"
                            )

                        with col2:

                            st.metric(
                                "Vento",
                                f"{clima['wind_speed_10m']} km/h"
                            )

                            st.metric(
                                "Precipitação",
                                f"{clima['precipitation']} mm"
                            )

                        st.caption(
                            "Dados meteorológicos fornecidos pela Open-Meteo. "
                            "A consulta representa a localização aproximada "
                            "da cidade, não necessariamente o endereço exato."
                        )

                    else:

                        st.warning(
                            "Não foi possível localizar as coordenadas "
                            "da cidade para consultar o clima."
                        )

        except requests.exceptions.Timeout:

            st.error("A API demorou para responder. Tente novamente.")

        except requests.exceptions.RequestException:

            st.error(
                "Erro de conexão com uma das APIs. "
                "Verifique sua internet e tente novamente."
            )

        except (KeyError, ValueError):

            st.error(
                "Não foi possível interpretar os dados retornados pela API."
            )

        except Exception:

            st.error(
                "Ocorreu um erro inesperado durante a consulta."
            )


# =====================================
# RODAPÉ
# =====================================

st.divider()

st.caption(
    "Localiza+ | Desenvolvido com Python e Streamlit"
)
