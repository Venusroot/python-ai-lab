# programadores = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']
# print(type(programadores))  # type ‘list’
# print(len(programadores))  # 5
# print(programadores[4])  # Luana

# ================================================================

# programadores = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']
# print(programadores) # ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']

# programadores[1] = 'Carolina'
# print(programadores) # ['Victor', 'Carolina', 'Samuel', 'Caio', 'Luana']

# ================================================================

# dados_cliente = {
#     'Nome': 'Renan',
#     'Endereco': 'Rua Cruzeiro do Sul',
#     'Telefone': '982503645'
#     }

# print(dados_cliente['Endereco']) # Renan ou Rua Cruzeiro do Sul

# ================================================================

# dados_cliente = {
#     'Nome': 'Renan',
#     'Endereco': 'Rua Cruzeiro do Sul',
#     'Telefone': '982503645' }
# print(dados_cliente)

# dados_cliente['Idade'] = 40
# print(dados_cliente)

# ================================================================

# professores = ['Carla', 'Daniel', 'Ingrid', 'Roberto']
# estacoes = ('Primavera', 'Verão', 'Outono', 'Inverno')
# cliente = { 'Nome': 'Fábio Garcia', 'email' : 'fabio_garcia_9@outlook.com' }

# print(type(professores))#list
# print(type(estacoes)) # tuple
# print(type(cliente)) # dict

# =======================================================================
# # Uma lista onde cada item é uma string (texto)
# tarefas_do_dia = ['Lavar a louça', 'Estudar Python', 'Ir à academia', 'Fazer compras']

# # Adicionar uma nova tarefa
# tarefas_do_dia.append('Ler um livro') #appemd serve para adicionar dados na lista 

# print("Minhas tarefas para hoje:")
# for tarefa in tarefas_do_dia:
#     print(f"- {tarefa}")

# ===================================================================

# #Formato: [Nome do Produto, Quantidade em estoque, Preço, Disponível]
# produto = ['Notebook Dell', 15, 4599.90, True]

# nome = produto[0]
# preco = produto[2]

# print(f"O produto '{nome}' custa R${preco:.2f}.")


# ============================================================
# numeros_pares = [] # Começamos com uma lista vazia
# numeros_impares = []

# print("Digite 5 números e eu mostrarei os pares e impares.")

# for i in range(5):
#     numero = int(input(f"Digite o {i+1}º número: "))
#     if numero % 2 == 0: # Verifica se o número é par
#         numeros_pares.append(numero)

#     elif numero % 2 == 1: # Verifica se o número é impar
#         numeros_impares.append(numero)

# print(f"\nOs números pares que você digitou foram: {numeros_pares}")
# print(f"Os números impares que você digitou foram: {numeros_impares}")
