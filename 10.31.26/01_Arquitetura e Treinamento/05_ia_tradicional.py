# **A) Exemplo de IA Tradicional (Classificador de Sentimentos)**
# Este script simula uma IA que apenas classifica uma entrada em "Positivo" ou "Negativo" com base em regras pré-definidas.


# IA Tradicional: Apenas classifica o que recebe
def classificador_tradicional(texto):
    palavras_positivas = ["bom", "excelente", "ótimo", "ajudou"]
    
    # Lógica de classificação (Se contém a palavra, é positivo)
    if any(palavra in texto.lower() for palavra in palavras_positivas):
        return "Saída: Classificado como POSITIVO"
    else:
        return "Saída: Classificado como NEGATIVO ou NEUTRO"

# Teste
entrada = "O curso de Python do SENAI é muito bom!"
print(f"Entrada: {entrada}")
print(classificador_tradicional(entrada)) # Apenas classifica
