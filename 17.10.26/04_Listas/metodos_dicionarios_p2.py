# metodos aplicados em dicionários

def main():
    # Chaves e valores - É o nome que da para as infomações
    cadastro = {
        "nome":         "Jairo",
        "sobrenome":    "Candido",
        "endereco":     "Rua Luis Lacava",
        "cidade":       "Mauá",
        "estado":       "São Paulo"
    }

    # print(cadastro) # dict completo

    # print(cadastro.keys()) # chama somente as chaves
    # print(cadastro.values()) # chama somente os valores

    # valor1 = cadastro["nome"]
    # print (valor1)

    # valor2 = cadastro["sobrenome"]
    # print (valor2)

    # valor2 = cadastro.get("sobrenome")
    # print(valor2)

    # cadastro.clear()
    # print(cadastro)


if __name__ == "__main__":
    main()
