# *B) Exemplo de IA Generativa (Simulador de Predição de Palavras)**
# Este script ilustra o conceito de **LLM (Large Language Model):** 

# A IA não pesquisa a resposta, ela calcula qual é a próxima palavra mais provável com base em um "treinamento" (neste caso, um pequeno dicionário de probabilidades).

import random

# Simulação de "Conhecimento Treinado" (Probabilidades)
# A IA "aprendeu" que depois de certas palavras, outras costumam vir.
memoria_treinada = {
    "O": ["ChatGPT", "SENAI", "Python"],
    "ChatGPT": ["é", "gera", "ajuda"],
    "é": ["incrível", "uma IA", "útil"],
    "Python": ["é", "ajuda", "facilita"]
}

def gerador_generativo(prompt_inicial, tamanho=3):
    frase = [prompt_inicial]
    palavra_atual = prompt_inicial
    
    for _ in range(tamanho):
        if palavra_atual in memoria_treinada:
            # IA escolhe a próxima palavra baseada nas probabilidades aprendidas
            proxima = random.choice(memoria_treinada[palavra_atual])
            frase.append(proxima)
            palavra_atual = proxima
        else:
            break
            
    return " ".join(frase)

# Teste
prompt = "O"
print(f"\nPrompt: {prompt}")

# A IA cria algo novo com base no que "sabe" (conhecimento congelado)
print(f"Saída Generativa: {gerador_generativo(prompt)}")




