
# ==========================================
# SISTEMA DE GERENCIAMENTO DE PRODUTOS
# Princípio DRY - Don't Repeat Yourself
# ==========================================

produtos = [
    {"nome": "Mouse", "preco": 50.0, "quantidade": 10},
    {"nome": "Teclado", "preco": 150.0, "quantidade": 5},
    {"nome": "Monitor", "preco": 800.0, "quantidade": 2},
    {"nome": "Cadeira Gamer", "preco": 900.0, "quantidade": 3},
    {"nome": "Headphone", "preco": 85.0, "quantidade": 4}
]


# 1. Função para calcular o valor total
def calcular_total(produto):
    return produto["preco"] * produto["quantidade"]


# 2. Listar todos os produtos
def listar_produtos():
    print("\n========== LISTA DE PRODUTOS ==========")

    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for i, produto in enumerate(produtos, start=1):
        total = calcular_total(produto)

        print(f"\nCódigo: {i}")
        print(f"Nome: {produto['nome']}")
        print(f"Preço: R$ {produto['preco']:.2f}")
        print(f"Quantidade: {produto['quantidade']}")
        print(f"Valor total: R$ {total:.2f}")


# 3. Cadastrar um novo produto
def cadastrar_produto():
    print("\n========== CADASTRAR PRODUTO ==========")

    nome = input("Nome do produto: ").strip()

    if not nome:
        print("Nome inválido!")
        return

    try:
        preco = float(input("Preço: R$ "))
        quantidade = int(input("Quantidade: "))

        if preco < 0 or quantidade < 0:
            print("Preço e quantidade não podem ser negativos!")
            return

        produto = {
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        }

        produtos.append(produto)
        print(f"\nProduto '{nome}' cadastrado com sucesso!")

    except ValueError:
        print("Digite valores numéricos válidos!")


# 4. Pesquisar produtos pelo nome
def pesquisar_produto():
    print("\n========== PESQUISAR PRODUTO ==========")

    busca = input("Digite o nome do produto: ").strip().lower()

    encontrados = [
        produto for produto in produtos
        if busca in produto["nome"].lower()
    ]

    if encontrados:
        print(f"\nEncontrados: {len(encontrados)} produto(s)")

        for produto in encontrados:
            print(f"\nNome: {produto['nome']}")
            print(f"Preço: R$ {produto['preco']:.2f}")
            print(f"Quantidade: {produto['quantidade']}")
            print(f"Total: R$ {calcular_total(produto):.2f}")
    else:
        print("Nenhum produto encontrado.")


# 5. Atualizar um produto
def atualizar_produto():
    print("\n========== ATUALIZAR PRODUTO ==========")

    pesquisar = input("Nome do produto que deseja atualizar: ").strip().lower()

    encontrados = [
        (i, produto) for i, produto in enumerate(produtos)
        if pesquisar in produto["nome"].lower()
    ]

    if not encontrados:
        print("Produto não encontrado!")
        return

    for i, produto in encontrados:
        print(f"{i + 1} - {produto['nome']}")

    try:
        codigo = int(input("Digite o código do produto: ")) - 1

        if codigo < 0 or codigo >= len(produtos):
            print("Código inválido!")
            return

        produto = produtos[codigo]

        nome = input(f"Novo nome ({produto['nome']}): ").strip()
        preco = input(f"Novo preço ({produto['preco']}): ").strip()
        quantidade = input(
            f"Nova quantidade ({produto['quantidade']}): "
        ).strip()

        if nome:
            produto["nome"] = nome

        if preco:
            novo_preco = float(preco)
            if novo_preco < 0:
                print("Preço inválido!")
                return
            produto["preco"] = novo_preco

        if quantidade:
            nova_quantidade = int(quantidade)
            if nova_quantidade < 0:
                print("Quantidade inválida!")
                return
            produto["quantidade"] = nova_quantidade

        print("Produto atualizado com sucesso!")

    except ValueError:
        print("Valor inválido!")


# 6. Excluir produto
def excluir_produto():
    print("\n========== EXCLUIR PRODUTO ==========")

    pesquisar = input("Nome do produto: ").strip().lower()

    encontrados = [
        (i, produto) for i, produto in enumerate(produtos)
        if pesquisar in produto["nome"].lower()
    ]

    if not encontrados:
        print("Produto não encontrado!")
        return

    for i, produto in encontrados:
        print(f"{i + 1} - {produto['nome']}")

    try:
        codigo = int(input("Código do produto que deseja excluir: ")) - 1

        if codigo < 0 or codigo >= len(produtos):
            print("Código inválido!")
            return

        nome = produtos[codigo]["nome"]
        confirmar = input(f"Confirma excluir {nome}? (s/n): ").lower()

        if confirmar == "s":
            produtos.pop(codigo)
            print("Produto excluído com sucesso!")
        else:
            print("Exclusão cancelada.")

    except ValueError:
        print("Código inválido!")


# 7. Exibir resumo do estoque
def resumo_estoque():
    print("\n========== RESUMO DO ESTOQUE ==========")

    quantidade_produtos = len(produtos)
    quantidade_itens = sum(p["quantidade"] for p in produtos)
    valor_estoque = sum(calcular_total(p) for p in produtos)

    print(f"Produtos cadastrados: {quantidade_produtos}")
    print(f"Total de unidades: {quantidade_itens}")
    print(f"Valor total do estoque: R$ {valor_estoque:.2f}")


# 8. Menu principal
def menu():
    while True:
        print("""
========================================
       SISTEMA DE PRODUTOS
========================================

1 - Listar produtos
2 - Cadastrar produto
3 - Pesquisar produto
4 - Atualizar produto
5 - Excluir produto
6 - Resumo do estoque
0 - Sair

========================================
""")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar_produtos()

        elif opcao == "2":
            cadastrar_produto()

        elif opcao == "3":
            pesquisar_produto()

        elif opcao == "4":
            atualizar_produto()

        elif opcao == "5":
            excluir_produto()

        elif opcao == "6":
            resumo_estoque()

        elif opcao == "0":
            print("Sistema encerrado. Até mais!")
            break

        else:
            print("Opção inválida! Tente novamente.")


# Executar o sistema
if __name__ == "__main__":
    menu()
