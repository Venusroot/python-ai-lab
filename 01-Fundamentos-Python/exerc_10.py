"""
Teste Final  Simulador de Caixa de Loja

Você foi contratado para desenvolver um sistema simples de caixa para uma pequena loja.
Seu desafio é criar um programa em Python que simule uma compra com três produtos e forneça um resumo da compra ao cliente.

O QUE O PROGRAMA DEVE FAZER:

Pedir o nome do cliente
Pedir o nome e o preço de 3 produtos
Calcular o valor total da compra
Aplicar um desconto de 5% sobre o total
Calcular o valor final dividido em 2x sem juros

Exibir um resumo completo, com:

Nome do cliente
Lista dos produtos e preços
Valor total da compra (sem desconto)
Valor do desconto
Valor total com desconto
Valor de cada parcela (2x)

Mensagem de agradecimento personalizada

DICAS IMPORTANTES:
Use variáveis para armazenar todos os valores
Use operadores matemáticos para fazer os cálculos
Organize a saída do programa para ficar fácil de ler

EXEMPLO DE SAÍDA ESPERADA:

RESUMO DA COMPRA   

Cliente: Ana Souza  
Produtos comprados:  
- Camiseta - R$ 50.00  
- Calça - R$ 120.00  
- Tênis - R$ 200.00  
--------------------------------
Total Compra: R$ 370.0  
Desconto (5%): R$ 18.5  
Total com desconto: R$ 351.5  
Pagamento em 2x de: R$ 175.75 

"""

import os

def limpar_tela():
    #Função responsavél por limpar a tela do terminal, após usuario digitar as informações
    os.system('cls' if os.name == 'nt' else 'clear')

cliente = (input('\nDigite o nome do cliente: '))

produto1  = (input('\nDigite o nome 1° produto: '))
valor1    = float (input('Digite o valor do 1° produto: '))

produto2  = (input('\nDigite o nome 2° produto: '))
valor2    = float (input('Digite o valor do 2° produto: '))

produto3  = (input('\nDigite o nome 3° produto: '))
valor3    = float (input('Digite o valor do 3° produto: '))

#Aplicando função para limpar a tela
limpar_tela()

#Processamento
total = valor1 + valor2 + valor3

print(f'\n           CAIXA DA LOJA         ')

print('-'*40)
print(f'Cliente: {cliente}')
print('-'*40)

print(f'\n => {produto1}  R$: {valor1:.2f}') 
print(f' => {produto2}  R$: {valor2:.2f}') 
print(f' => {produto3}  R$: {valor3:.2f}') 

print('________________________________________')

print(f'\n Total da compra: R$ {total:.2f}')
print(f' Desconto(5%): R$ {(total*0.05):.2f}')
print(f' Total com desconto: R$ {total-(total*0.05):.2f}')
print(f' Pagamento em 2x de: R$ {(total-(total*0.05))/2:.2f}')

print('\n________________________________________')

print(f'\nAgradecemos sua compra!!')

print('\n')







