# O bloco try contém o código que pode gerar uma exceção.
# o bloco except contém o código que será executado caso a exceção ocorra. 
import random

numero_secreto = random.randint(1, 50)
palpite = 0

print("Jogo de Adivinhação! Tente adivinhar o número entre 1 e 50.")

# Enquanto o 'palpite' do usuário for diferente do 'numero_secreto'...
while palpite != numero_secreto:
    # ...peça um novo palpite.
    try:
        palpite = int(input("\nQual o seu palpite? "))
        
        if palpite < numero_secreto:
            print("Muito baixo! Tente novamente.")
        elif palpite > numero_secreto:
            print("Muito alto! Tente novamente.")
    except ValueError: # neste caso, por conta de algo digitado fora do contexto (caractere especial ou letras)
        print("Por favor, digite um número válido.")

print("=" * 30) # Serve para multiplicar os traços para poder ter uma linha
print(f"Parabéns! Você acertou! O número secreto era {numero_secreto}.")

