
"""
Dicionario

Exercício 1: Atualização de Cadastro de Clientes (Setor de CRM) 
Você tem um dicionário com o faturamento acumulado de alguns clientes: 
clientes = {"Carlos": 5000, "Pedro": 3000, "Jorge": 4500}. O cliente "Carlos" fez uma nova compra de R$ 1.500,00. 

Crie um código que: 
	1. Atualize o valor do cliente "Carlos" somando o novo valor ao faturamento antigo. 
	2. Adicione um novo cliente chamado "Marcos" com um faturamento inicial de R$  2.000,00. 
	3. Exiba o dicionário atualizado.

    """

# Cria um dicionario com os nomes dos clientes e vlores de compra
clientes = {"Carlos": 5000, "Pedro": 3000, "Jorge": 4500}

# Define o valor de uma nova compra realizada por um cliente
nova_compra = 1500

# Atualizar o valor totl de compras do cliente "Carlos"
clientes["Carlos"] = clientes["Carlos"] + nova_compra

# Adicionar um novo cliente chamado "Marcos" ao dicionario
# com o valor inicial de compras igual a 2000
clientes["Marcos"] = 2000

print(clientes)
