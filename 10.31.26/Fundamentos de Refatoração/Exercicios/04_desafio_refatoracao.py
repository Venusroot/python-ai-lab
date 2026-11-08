
"""
Sistema de Vendas - Versão Refatorada

Este programa calcula o faturamento dos produtos,
aplica descontos e verifica a disponibilidade de estoque.
"""


def calcular_total(preco_unitario, quantidade, desconto):
    """
    Calcula o valor total de uma venda após aplicar o desconto.

    Args:
        preco_unitario (float): Preço de cada unidade.
        quantidade (int): Quantidade de produtos vendidos.
        desconto (float): Valor do desconto em reais.

    Returns:
        float: Valor total da venda.
    """
    subtotal = preco_unitario * quantidade

    if desconto < 0:
        raise ValueError("O desconto não pode ser negativo.")

    if desconto > subtotal:
        raise ValueError("O desconto não pode ser maior que o subtotal.")

    return subtotal - desconto


def verificar_estoque(quantidade):
    """
    Verifica se existe quantidade disponível para a venda.

    Args:
        quantidade (int): Quantidade de produtos disponíveis.

    Returns:
        str: Situação do estoque.
    """
    if quantidade <= 0:
        return "Produto sem estoque."

    return "Produto disponível em estoque."


def processar_vendas(lista_vendas):
    """
    Processa as vendas, calcula os valores e apresenta os resultados.

    Args:
        lista_vendas (list): Lista contendo os dados dos produtos.
    """
    faturamento_total = 0

    print("========= SISTEMA DE VENDAS =========\n")

    for venda in lista_vendas:
        try:
            nome_produto, preco_unitario, quantidade, desconto = venda

            # Conversão dos dados para os tipos corretos
            preco_unitario = float(preco_unitario)
            quantidade = int(quantidade)
            desconto = float(desconto)

            # Validação dos dados
            if preco_unitario < 0 or quantidade < 0:
                raise ValueError("Preço e quantidade não podem ser negativos.")

            # Cálculo da venda
            total_venda = calcular_total(
                preco_unitario,
                quantidade,
                desconto
            )

            faturamento_total += total_venda

            print(f"Produto: {nome_produto}")
            print(f"Preço unitário: R$ {preco_unitario:.2f}")
            print(f"Quantidade: {quantidade}")
            print(f"Desconto: R$ {desconto:.2f}")
            print(f"Total da venda: R$ {total_venda:.2f}")

            # Verificação do estoque
            situacao_estoque = verificar_estoque(quantidade)
            print(f"Estoque: {situacao_estoque}")

            # Evita divisão por zero
            if quantidade > 0:
                preco_medio = total_venda / quantidade
                print(f"Preço médio por item: R$ {preco_medio:.2f}")

            print("-" * 40)

        except ValueError as erro:
            print(f"Erro ao processar o produto: {erro}")
            print("-" * 40)

        except (TypeError, IndexError) as erro:
            print(f"Dados inválidos na venda: {erro}")
            print("-" * 40)

    print("\n========= RESUMO FINANCEIRO =========")
    print(f"Faturamento total: R$ {faturamento_total:.2f}")
    print("=====================================")


# Dados das vendas
vendas = [
    ["Mouse", 50, 2, 10],
    ["Teclado", 150, 1, "5"],
    ["Monitor", 800, 0, 0]
]

# Execução do sistema
if __name__ == "__main__":
    processar_vendas(vendas)
