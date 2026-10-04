"""
07. Solicite ao usuario a valor do salario atual,
em seguida solicite o precentual de aumento e imprima o valor
do salario atual

"""
nome = (input('\nDigite o seu nome: '))

salario_atual = float (input('\nDigite o valor do seu Salario Atual: '))
percentual    = float (input('Qual será o percentual de aumento: '))

aumento = salario_atual * (percentual/100)
salario_atual = salario_atual + aumento

print(f'\n{nome} o seu salario agora é R$: {salario_atual:.2f}') 
print(f'E o aumento foi de R$: {aumento:.2f}') 
