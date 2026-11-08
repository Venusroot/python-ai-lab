
def simulador_tokenizer(texto):
    tokens = [texto[i:i+3] for i in range(0, len(texto), 3)]

    return tokens


print("=" * 45)
print("       SIMULADOR DE TOKENIZAÇÃO")
print("=" * 45)

# Entrada do usuário
texto = input("\nDigite uma frase ou texto: ")

# Processamento
tokens = simulador_tokenizer(texto)

# Estatísticas
caracteres = len(texto)
palavras = len(texto.split())
quantidade_tokens = len(tokens)
espacos = texto.count(" ")
vogais = sum(1 for letra in texto.lower() if letra in "aeiou")
numeros = sum(1 for letra in texto if letra.isdigit())

# Relatório
print("\n" + "=" * 45)
print("          RELATÓRIO DE ANÁLISE")
print("=" * 45)

print(f"\nTexto digitado: {texto}")

print("\n--- ESTATÍSTICAS ---")
print(f"Total de caracteres: {caracteres}")
print(f"Total de palavras: {palavras}")
print(f"Total de espaços: {espacos}")
print(f"Total de vogais: {vogais}")
print(f"Total de números: {numeros}")
print(f"Total de tokens: {quantidade_tokens}")

print("\n--- TOKENS IDENTIFICADOS ---")

for i, token in enumerate(tokens, 1):
    print(f"Token {i}: [{token}]")

print("\n" + "=" * 45)
print("       ANÁLISE CONCLUÍDA!")
print("=" * 45)
