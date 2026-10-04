"""
09. crie um programa que solicite o nome do funcionario,
as horas trabalhadas no mes e o valor que recebe por hora.
Depois, calcule:

salario_bruto (horas * valor_por_hora)
Desconto de 11% de imposto = 0.11
salario_liquido (salario_bruto - imposto)

Ao exibir o resultado, as informações digitadas deve ser
apagadas, mantendo apenas os prints coma informações na tela

Windows + . -> emojis

"""
import os

def limpar_tela():
    #Função responsavél por limpar a tela do terminal, após usuario digitar as informações
    os.system('cls' if os.name == 'nt' else 'clear')


nome = (input('\nDigite o seu nome: '))

horas    = int (input('\nDigite quantas as horas trabalhadas: '))
valor_hr = float (input('Digite o valor da hora trabalhada: '))

#Aplicando função para limpar a tela
limpar_tela()

#Processamento da solicitação
salario_bruto   = (horas * valor_hr)
imposto         = (salario_bruto * 0.11)
salario_liquido = salario_bruto - imposto

#Imprimindo resposta ao usuario

print(f'\n{nome} o seu salario bruto é R$: {salario_bruto:.2f}') 
print(f'O desconto do mês é R$: {imposto:.2f}') 

print(f'\nSalário liquido é R$: {salario_liquido:.2f}') 

# Se quiser adicionar o tracinho posso adicionar o print ('-'*30)