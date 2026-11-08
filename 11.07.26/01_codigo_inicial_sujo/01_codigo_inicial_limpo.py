# Função para somar duas idades
def somar_idades(idade_a, idade_b):
    resultado = idade_a + idade_b
    return resultado


# Lista com os pares de idades
idades = [
    {"idade1": 20, "idade2": 25},
    {"idade1": 30, "idade2": 35}
]


# Percorre a lista e realiza as somas
for par in idades:
    soma = somar_idades(par["idade1"], par["idade2"])
    print(soma)
