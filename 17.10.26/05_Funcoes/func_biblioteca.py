# def é palavra-chave usada para definir funções.
# Funções são blocos de código reutilizaveis que executam tarefas especificas,
# e a definição com def permite organizar o código, evitar repetição.

# Biblioteca de funções - Coleção de funções
# Bibliotecas vao ter funções com a mesma finalidade

# def nomeFuncao("argumento da funcao - o que a necessita de informação"):
#   # O que a função irá fazer
#   return ('resposta da função)

def soma(num1, num2):
    res = num1 + num2
    return res

def sub(num1, num2):
    res = num1 - num2
    return res

def mult(num1, num2):
    res = num1 * num2
    return res

def div(num1, num2):
    res = num1 / num2
    return res

def expo(num1, num2):
    res = num1 ** num2
    return res

def imprimirResultado(res):
    print(f"O resultado da operação é : ", res)
