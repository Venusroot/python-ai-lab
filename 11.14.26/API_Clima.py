
import streamlit as st
import requests

from datetime import datetime


# =====================================
# CONFIGURAÇÃO
# =====================================

st.set_page_config(
    page_title="Localiza+ | Clima",
    page_icon="🌤️",
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

.clima {
    background-color: #FFF8F2;
    padding: 22px;
    border-radius: 12px;
    border: 1px solid #F5E2D3;
    text-align: center;
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
# FUNÇÃO: OBTER CLIMA
# =====================================

def obter_clima(latitude, longitude):

    url = "https://api.open-meteo.com/v1/forecast"

    parametros = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m",
        "timezone": "auto"
    }

    resposta = requests.get(
        url,
        params=parametros,
        timeout=10
    )

    resposta.raise_for_status()

    dados = resposta.json()

    if "current" not in dados:

        return None

    return dados["current"]


# =====================================
# INTERFACE
# =====================================

st.title("🌤️ Localiza+")

st.caption(
    "Consulte as condições climáticas de uma cidade."
)

st.divider()

st.subheader("Consulta meteorológica")

cidade = st.text_input(
    "Digite o nome da cidade",
    placeholder="Exemplo: Curitiba"
)

if st.button("Consultar clima"):

    if not cidade.strip():

        st.warning("Digite o nome de uma cidade.")

    else:

        try:

            with st.spinner("Localizando cidade..."):

                resultados = buscar_coordenadas(
                    cidade.strip()
                )

            if not resultados:

                st.warning("Cidade não encontrada.")

            else:

                opcoes = [
                    f"{r.get('name', 'Não informado')} - "
                    f"{r.get('admin1', 'Região não informada')} - "
                    f"{r.get('country', 'País não informado')}"
                    for r in resultados
                ]

                indice = st.selectbox(
                    "Selecione a cidade",
                    range(len(opcoes)),
                    format_func=lambda i: opcoes[i]
                )

                local = resultados[indice]

                with st.spinner("Consultando condições climáticas..."):

                    clima = obter_clima(
                        local["latitude"],
                        local["longitude"]
                    )

                if clima is None:

                    st.warning("Não foi possível obter o clima.")

                else:

                    # CONVERSÃO DO HORÁRIO

                    horario = datetime.fromisoformat(
                        clima["time"]
                    )

                    horario_formatado = horario.strftime(
                        "%d/%m/%Y às %H:%M"
                    )

                    st.success("Consulta realizada!")

                    st.divider()

                    st.subheader("📍 Localização")

                    st.write(
                        f"**Cidade:** {local['name']}"
                    )

                    st.write(
                        f"**Estado/Região:** "
                        f"{local.get('admin1', 'Não informado')}"
                    )

                    st.write(
                        f"**País:** {local.get('country', 'Não informado')}"
                    )

                    st.divider()

                    st.subheader("🌤️ Condições atuais")

                    st.markdown(
                        f"""
                        <div class="clima">
                            <h1 style="color:#E98243 !important;">
                                {clima['temperature_2m']} °C
                            </h1>
                            <p>Temperatura atual</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    col1, col2 = st.columns(2)

                    with col1:

                        st.metric(
                            "Velocidade do vento",
                            f"{clima['wind_speed_10m']} km/h"
                        )

                    with col2:

                        st.metric(
                            "Horário da consulta",
                            horario.strftime("%H:%M")
                        )

                    st.caption(
                        f"Data e hora dos dados meteorológicos: "
                        f"{horario_formatado}"
                    )

                    st.caption(
                        "Fonte: Open-Meteo. Os dados representam "
                        "a localização aproximada da cidade."
                    )

        except requests.exceptions.Timeout:

            st.error("Tempo limite de conexão excedido.")

        except requests.exceptions.RequestException:

            st.error("Erro ao conectar com uma das APIs.")

        except (KeyError, ValueError):

            st.error("Erro ao processar os dados recebidos.")

# =====================================
# RODAPÉ
# =====================================

st.divider()

st.caption("Localiza+ | Clima com Open-Meteo")
