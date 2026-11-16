
import streamlit as st
import requests

from datetime import datetime


# =====================================
# CONFIGURAÇÃO DA PÁGINA
# =====================================

st.set_page_config(
    page_title="Localiza+ | Clima e Geolocalização",
    page_icon="📍",
    layout="centered"
)


# =====================================
# ESTILIZAÇÃO CSS
# =====================================

st.markdown("""
<style>

.stApp {
    background-color: #FFFFFF;
}

.main .block-container {
    padding-top: 2rem;
}

h1, h2, h3, h4 {
    color: #292929 !important;
}

p, label {
    color: #555555 !important;
}

.stButton > button {
    background-color: #E98243 !important;
    color: #FFFFFF !important;
    border: none;
    border-radius: 8px;
    height: 45px;
    font-weight: 600;
    width: 100%;
}

.stButton > button:hover {
    background-color: #D96F30 !important;
    color: #FFFFFF !important;
}

.card {
    background-color: #FFF8F2;
    padding: 18px;
    border-radius: 10px;
    border: 1px solid #F5E2D3;
    margin-bottom: 10px;
}

.clima {
    background-color: #FFF8F2;
    padding: 25px;
    border-radius: 12px;
    border: 1px solid #F5E2D3;
    text-align: center;
}

hr {
    border-color: #EEEEEE;
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
# FUNÇÃO: CONSULTAR CLIMA
# =====================================

def obter_clima(latitude, longitude):

    url = "https://api.open-meteo.com/v1/forecast"

    parametros = {
        "latitude": latitude,
        "longitude": longitude,
        "current": (
            "temperature_2m,"
            "wind_speed_10m,"
            "weather_code,"
            "is_day"
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

    return dados.get("current")


# =====================================
# FUNÇÃO: IDENTIFICAR CONDIÇÃO CLIMÁTICA
# =====================================

def identificar_clima(codigo, is_day):

    condicoes = {

        0: ("Céu limpo", "☀️" if is_day else "🌙"),

        1: ("Predominantemente limpo", "🌤️" if is_day else "🌙"),

        2: ("Parcialmente nublado", "⛅"),

        3: ("Nublado", "☁️"),

        45: ("Neblina", "🌫️"),
        48: ("Neblina com geada", "🌫️"),

        51: ("Garoa leve", "🌦️"),
        53: ("Garoa moderada", "🌦️"),
        55: ("Garoa intensa", "🌧️"),

        56: ("Garoa congelante leve", "🌧️"),
        57: ("Garoa congelante intensa", "🌧️"),

        61: ("Chuva leve", "🌦️"),
        63: ("Chuva moderada", "🌧️"),
        65: ("Chuva intensa", "🌧️"),

        66: ("Chuva congelante leve", "🌧️"),
        67: ("Chuva congelante intensa", "🌧️"),

        71: ("Neve leve", "🌨️"),
        73: ("Neve moderada", "❄️"),
        75: ("Neve intensa", "❄️"),

        77: ("Grãos de neve", "🌨️"),

        80: ("Pancadas de chuva leves", "🌦️"),
        81: ("Pancadas de chuva moderadas", "🌧️"),
        82: ("Pancadas de chuva fortes", "⛈️"),

        85: ("Pancadas de neve leves", "🌨️"),
        86: ("Pancadas de neve fortes", "❄️"),

        95: ("Tempestade", "⛈️"),
        96: ("Tempestade com granizo leve", "⛈️"),
        99: ("Tempestade com granizo forte", "⛈️")

    }

    return condicoes.get(
        codigo,
        ("Condição desconhecida", "🌡️")
    )


# =====================================
# CABEÇALHO
# =====================================

st.title("📍 Localiza+")

st.caption(
    "Geolocalização e condições climáticas "
    "em um só lugar."
)

st.divider()


# =====================================
# CAMPO DE PESQUISA
# =====================================

st.subheader("Consultar localização")

cidade = st.text_input(
    "Nome da cidade",
    placeholder="Digite uma cidade. Ex: São Paulo"
)

consultar = st.button("Consultar informações")


# =====================================
# PROCESSAMENTO
# =====================================

if consultar:

    if not cidade.strip():

        st.warning(
            "Por favor, digite o nome de uma cidade."
        )

    else:

        try:

            # BUSCAR LOCALIZAÇÃO

            with st.spinner("Buscando localização..."):

                resultados = buscar_coordenadas(
                    cidade.strip()
                )

            if not resultados:

                st.warning("Nenhuma cidade encontrada.")

            else:

                # SELEÇÃO DE CIDADES

                opcoes = [
                    f"{r.get('name', 'Não informado')} - "
                    f"{r.get('admin1', 'Região não informada')} - "
                    f"{r.get('country', 'País não informado')}"
                    for r in resultados
                ]

                indice = st.selectbox(
                    "Selecione a cidade desejada",
                    range(len(opcoes)),
                    format_func=lambda i: opcoes[i],
                    key="cidade_escolhida"
                )

                local = resultados[indice]

                latitude = local["latitude"]
                longitude = local["longitude"]

                # CONSULTAR CLIMA

                with st.spinner("Consultando clima..."):

                    clima = obter_clima(
                        latitude,
                        longitude
                    )

                if clima is None:

                    st.warning(
                        "Não foi possível obter os dados climáticos."
                    )

                else:

                    # FORMATAR DATA

                    horario = datetime.fromisoformat(
                        clima["time"]
                    )

                    horario_formatado = horario.strftime(
                        "%d/%m/%Y às %H:%M"
                    )

                    st.success(
                        "Consulta realizada com sucesso!"
                    )

                    st.divider()

                    # =====================================
                    # INFORMAÇÕES GEOGRÁFICAS
                    # =====================================

                    st.subheader("🗺️ Informações geográficas")

                    col1, col2 = st.columns(2)

                    with col1:

                        st.markdown(
                            f"""
                            <div class="card">
                                <small>Latitude</small>
                                <h3>{latitude}</h3>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    with col2:

                        st.markdown(
                            f"""
                            <div class="card">
                                <small>Longitude</small>
                                <h3>{longitude}</h3>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    st.write(
                        f"**Cidade:** {local.get('name', 'Não informado')}"
                    )

                    st.write(
                        f"**Estado/Região:** "
                        f"{local.get('admin1', 'Não informado')}"
                    )

                    st.write(
                        f"**País:** {local.get('country', 'Não informado')}"
                    )

                    st.write(
                        f"**Código do país:** "
                        f"{local.get('country_code', 'Não informado')}"
                    )

                    st.divider()

                    # =====================================
                    # INFORMAÇÕES CLIMÁTICAS
                    # =====================================

                    st.subheader("🌤️ Condições climáticas")

                    descricao, icone = identificar_clima(
                        clima["weather_code"],
                        clima["is_day"]
                    )

                    # TEMPERATURA E ÍCONE

                    col1, col2 = st.columns([1, 2])

                    with col1:

                        st.markdown(
                            f"""
                            <div style="
                                background-color: #FFF8F2;
                                border: 1px solid #F5E2D3;
                                border-radius: 12px;
                                padding: 20px;
                                text-align: center;
                            ">
                                <div style="font-size: 65px;">
                                    {icone}
                                </div>
                                <p style="color:#666666;">
                                    {descricao}
                                </p>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    with col2:

                        st.markdown(
                            f"""
                            <div style="
                                background-color: #FFF8F2;
                                border: 1px solid #F5E2D3;
                                border-radius: 12px;
                                padding: 20px;
                                text-align: center;
                            ">
                                <h1 style="
                                    color:#E98243 !important;
                                    font-size:45px;
                                    margin:0;
                                ">
                                    {clima['temperature_2m']}°C
                                </h1>
                                <p>Temperatura atual</p>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    st.write("")

                    # INFORMAÇÕES ADICIONAIS

                    col1, col2 = st.columns(2)

                    with col1:

                        st.metric(
                            "Velocidade do vento",
                            f"{clima['wind_speed_10m']} km/h"
                        )

                    with col2:

                        st.metric(
                            "Horário da medição",
                            horario.strftime("%H:%M")
                        )

                    st.caption(
                        f"Data e hora: {horario_formatado}"
                    )

                    st.caption(
                        "Fonte meteorológica: Open-Meteo."
                    )

                    st.divider()

                    # =====================================
                    # MAPA
                    # =====================================

                    st.subheader("📍 Mapa da localização")

                    st.map({
                        "latitude": [latitude],
                        "longitude": [longitude]
                    })

        # =====================================
        # TRATAMENTO DE ERROS
        # =====================================

        except requests.exceptions.Timeout:

            st.error(
                "A API demorou para responder. Tente novamente."
            )

        except requests.exceptions.RequestException as erro:

            st.error(
                f"Erro ao conectar com as APIs: {erro}"
            )

        except (KeyError, ValueError):

            st.error(
                "Não foi possível interpretar os dados recebidos."
            )

        except Exception as erro:

            st.error(
                f"Ocorreu um erro inesperado: {erro}"
            )


# =====================================
# RODAPÉ
# =====================================

st.divider()

st.caption(
    "Localiza+ | Python • Streamlit • Open-Meteo"
)
