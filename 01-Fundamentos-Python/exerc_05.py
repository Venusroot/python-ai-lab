"""
05 - crie um programa que recebe o valor, taxa e o tempo.
efetuar o calculo do valor de uma prestação em atraso.

FORMULA: 
prestacao = valor +(valor*(taxa/100)* tempo)
"""
#\n serve para pular linha

valor = float(input("Digite o valor da pestação: "))
taxa = float (input("Digite o valor da taxa: "))
tempo = int (input("Tempo do atraso em dias: "))

prestacao = valor + (valor*(taxa/100)*tempo)

print(f"O valor da sua prestação em atrado é: {prestacao:.2f}")
