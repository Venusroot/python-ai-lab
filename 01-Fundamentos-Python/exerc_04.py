"""
04 - Crie um programa para entrar com a base e a 
altura de um retangulo e imprima respectivamente o
perimetro e a area correspondente.

perimetro = 2 * (base+altura)
area = base * altura
"""

base = float(input('Digite o valor da base do retangulo: '))
altura = float(input('Digite o valor da altura do retangulo: '))

perimetro = 2 * (base+altura)
area = base * altura

print(f"O retangulo possui a area de {area} e base de {base}.")