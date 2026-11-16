import requests
from datetime import datetime

# ======================================================
# Funnção para buscar latitude e longitude de uma cidade

"""
Desenvolva um programa em Python que solicite ao usuário o nome de uma cidade e 
consulte as condições climáticas atuais utilizando as APIs do Open-Meteo. 
O sistema deve primeiro buscar as coordenadas geográficas (latitude e longitude) 
da cidade informada e, em seguida, utilizar essas coordenadas para obter os dados do clima atual. 
Organize a solução utilizando funções, trate possíveis erros de requisição com `try/except` e exiba 
ao final o nome da cidade, a temperatura atual, a velocidade do vento e o horário da consulta.
"""


def buscar_coordenadas(cidade):
    # URL da API de geolocalização do Open-Meteo
    # Essa API converte o nome de uma cidade em coordenadas geográficas.
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": cidade,  # nome da cidade digitada pelo usuario
        "count": 3  # retorna apenas o primeiro resultado encontrado
    }

    try:
        # faz a requisição GET para API
        # timeout=5 significa que a requisição aguardara 5 segundos maximo
        resposta = requests.get(url, params=params, timeout=5)

        # verifica se ocorreu algum erro HTPP (404, 500 etc.)
        resposta.raise_for_status()

        # Converte a resposta da API (JSON) PARA UM DICIONARIO PYTHON
        dados = resposta.json()

        # verificar se a chave "results" existe
        # e se ha algum resultado retornado
        if "results" not in dados or not dados["results"]:
            print("Cidade não Encontrada.")
            return None

        # obtem o primeiro resultado encontrado
        resultado = dados["results"][0]

        # Retorna latitude, longitude e nome da cidade
        return (
            resultado["latitude"],
            resultado["longitude"],
            resultado["name"]
        )

    # Capture erros relacionados a requisição
    except requests.exceptions.RequestException as e:
        print("Erro ao buscar coordenadas: ", e)
        return None

# =====================================================
# Função para obter informações do clima
# =====================================================


def obter_clima(latitude, longitude):

    # URL da API de previsão do tempo
    url = url = "https://api.open-meteo.com/v1/forecast"

    # Parametros enviados para a API
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True,
        "timezone": "auto"  # ajusta para o fuso horario local
    }
    try:
        # Realiza a requizição GET
        resposta = requests.get(url, params=params, timeout=5)

        # verifica se ocorreu algum erro HTPP (404, 500 etc.)
        resposta.raise_for_status()

        # Converte a resposta da API (JSON) PARA UM DICIONARIO PYTHON
        dados = resposta.json()

        # verifica se a chave "current_weather" existe
        if "current_weather" not in dados:
            print("Erro ao obter dados do clima.")
            return None
        # Retorna apenas os dados do clima atual
        return dados["current_weather"]

    # Capture erros de conexao ou requisição
    except requests.exceptions.RequestException as e:
        print("Erro na Requisição: ", e)
        return None

# =============================================================
# Programa Principal
# =============================================================


cidade = input("Digite o nome da cidade: ")

# chama a função para buscar as coordenadas da cidade
coords = buscar_coordenadas(cidade)

if coords:
    # desenpacotamento da tupla retornada
    latitude, longitude, nome_cidade = coords

    # busca os dados climaticos usando a latitude e longitude
    clima = obter_clima(latitude, longitude)

    # verifica se os dados do clima foram obtidos com sucesso
    if clima:
        # converte a data/hora da API para formato brasileiro
        horario = datetime.fromisoformat(clima["time"])
        horario_formatado = horario.strftime("%d/%m/%Y às %H:%M")

        # Exibe o nome da cidade
        print(f"\n📍 Cidade: {nome_cidade}")
        print(f"🌡️  Temperatura: {clima['temperature']} °C")
        print(f"🌬️  Vento: {clima['windspeed']} km/h")
        print(f"🕑  Data e Hora: {horario_formatado}")
