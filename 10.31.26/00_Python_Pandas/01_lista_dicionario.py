
# # Lista de dicionários (A estrutura padrão para DataFrames)
leituras_sensor = [
    {"timestamp": "2024-05-20 08:00", "sensor_id": 1, "temp": 22.5},
    {"timestamp": "2024-05-20 09:00", "sensor_id": 1, "temp": 23.1},
    {"timestamp": "2024-05-20 10:00", "sensor_id": 1, "temp": 24.8}
]

# # Mostrando como iterar (o que o Pandas faz internamente)
for leitura in leituras_sensor:
    print(f"No horário {leitura['timestamp']}, a temperatura foi de {leitura['temp']}°C")

#  -------------------------------------------------------------------------------

