"""
08. crie um programa que solicite dois numeros ao usuario e
mostre o resultado ds seguintes operações entre eles:

Resultado esperado:
Digite primeiro numero: xx
Digite segundo  numero: xx

Soma : xx
Subtração : xx
Multiplicação : xx
Divisão: xx
Divisão Inteira : xx
Resto da divisão : xx
Potencia : xx

# copia para baixo -> shift + alt + ↓

"""
import os

print("\n")
n1 = int (input('Digite o número 01: '))
n2 = int (input('Digite a núemro 02: '))
print("\n")

os.system('cls')

soma      =  n1 + n2
sub       =  n1 - n2
mult      =  n1 * n2
divisao   =  n1 / n2
resto     =  n1 % n2
potencia  =  n1 ** n2

print(f'A soma de {n1} + {n2} é: {soma:.2f}') 
print(f'A Subtração de {n1} - {n2} é: {sub:.2f}') 
print(f'A Multiplicação de {n1} x {n2} é: {mult:.2f}') 
print(f'A Divisão de {n1} / {n2} é: {divisao:.2f}') 
print(f'A Resto de {n1} e {n2} é: {resto:.2f}') 
print(f'A Potencia de {n1} ^{n2} é: {potencia:.2f}') 


"""
Outra opção era: print(f'A soma de {n1} + {n2} é: {n1+n2:.2f}')  
"""
