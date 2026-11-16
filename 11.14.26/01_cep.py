### Utilizando API no Python ####

import requests

cep = input("Digite o CEP: ").replace("-","").strip()

if len(cep) != 8 or not cep.isdigit():
    print("CEP invalido. Digite 8 numeros")

else:
    try:
        resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        dados = resposta.json()
        
        if "erro" in dados:
            print("CEP não encontrado.")
        else:
            for k, v in dados.items(): # k key v values
                print(f"{k}: {v}")
    
    except requests.exceptions.RequestException:
        print("Erro ao conectar com a API")




