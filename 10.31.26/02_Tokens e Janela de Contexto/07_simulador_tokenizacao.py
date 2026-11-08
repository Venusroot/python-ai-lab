# **A) Simulador de Tokenização**
# Este script mostra como a IA "enxerga" o texto de forma fragmentada para economizar processamento.


# Simulação de Tokenização (Quebrando em pedaços de 3 caracteres)
def simulador_tokenizer(texto):
    # Na vida real, a OpenAI usa o 'tiktoken', aqui simulamos a lógica
    tokens = [texto[i:i+3] for i in range(0, len(texto), 3)]
    return tokens

frase = "Programação com IA no SENAI"
lista_tokens = simulador_tokenizer(frase)

print(f"Frase original: {frase}")
print(f"A IA enxerga {len(lista_tokens)} tokens: {lista_tokens}")

