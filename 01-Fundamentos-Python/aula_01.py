nome = "Senai"      # String (texto)#
idade = 80          # int (Valor inteiro) Quando é numero não precisa de aspas
altura = 1.70       # float (decimal)
estudante = True    # bool (Boleano)

print(nome)
print(idade, altura, estudante)
print(type(altura))
print(type(idade))
print(type(nome))

# ---------------------------#
# Realizando input das variaveis com o Usuario
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

# Formatando os dados que será impresso 
print(f"Olá {nome}.")
print(f"Sua idade é {idade} anos.")
