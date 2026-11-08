
# ==========================================================
# SISTEMA DE GERENCIAMENTO DE VENDAS
# ==========================================================
# Conceitos:
# - Funções
# - Listas e dicionários
# - Laços de repetição
# - Tratamento de exceções
# - Docstrings
# - Clean Code
# - PEP 8
# ==========================================================


def calcular_total(preco, quantidade, desconto):
    """
    Calcula o valor total de uma venda aplicando desconto percentual.

    Args:
        preco (float): preço unitário do produto.
        quantidade (int): quantidade vendida.
        desconto (float): percentual de desconto.

    Returns:
        float: valor total da venda com desconto.
    """
    valor_bruto = preco * quantidade
    valor_desconto = valor_bruto * (desconto / 100)

    return valor_bruto - valor_desconto


def calcular_preco_medio(preco, quantidade):
    """
    Calcula o preço médio por unidade.

    Args:
        preco (float): preço unitário.
        quantidade (int): quantidade disponível ou vendida.

    Returns:
        float: preço médio por unidade.

    Raises:
        ValueError: se a quantidade for menor ou igual a zero.
    """
    if quantidade <= 0:
        raise ValueError("Quantidade deve ser maior que zero.")

    return (preco * quantidade) / quantidade


def processar_venda(venda):
    """
    Processa os dados de uma venda e apresenta seus resultados.

    Args:
        venda (dict): dados do produto e da venda.
    """
    nome = venda["nome"]
    preco = venda["preco"]
    quantidade = venda["quantidade"]
    desconto = venda["desconto"]

    total = calcular_total(preco, quantidade, desconto)

    print(f"\nProduto: {nome}")
    print(f"Preço unitário: R$ {preco:.2f}")
    print(f"Quantidade: {quantidade}")
    print(f"Desconto: {desconto:.2f}%")
    print(f"Total da venda: R$ {total:.2f}")

    if quantidade > 0:
        preco_medio = calcular_preco_medio(preco, quantidade)
        print(f"Preço médio por item: R$ {preco_medio:.2f}")
    else:
        print("Estoque indisponível: quantidade igual a zero.")

    print("-" * 45)


def validar_venda(venda):
    """
    Valida os dados recebidos para uma venda.

    Raises:
        ValueError: se algum dado estiver fora dos limites.
    """
    if not venda["nome"].strip():
        raise ValueError("Nome do produto não pode ficar vazio.")

    if venda["preco"] < 0:
        raise ValueError("O preço não pode ser negativo.")

    if venda["quantidade"] < 0:
        raise ValueError("A quantidade não pode ser negativa.")

    if not 0 <= venda["desconto"] <= 100:
        raise ValueError("O desconto deve estar entre 0 e 100%.")


def executar_sistema():
    """
    Executa o sistema de vendas, processando todos os produtos.

    Trata erros de conversão e validação individualmente.
    """
    vendas = [
        {
            "nome": "Mouse",
            "preco": 50.0,
            "quantidade": 2,
            "desconto": 10
        },
        {
            "nome": "Teclado",
            "preco": 150.0,
            "quantidade": 1,
            "desconto": "5"
        },
        {
            "nome": "Monitor",
            "preco": 800.0,
            "quantidade": 0,
            "desconto": 0
        }
    ]

    faturamento_total = 0

    print("\n===== SISTEMA DE VENDAS =====")

    for venda in vendas:
        try:
            # Conversão dos dados numéricos
            venda["preco"] = float(venda["preco"])
            venda["quantidade"] = int(venda["quantidade"])
            venda["desconto"] = float(venda["desconto"])

            # Validação dos dados
            validar_venda(venda)

            # Processamento da venda
            processar_venda(venda)

            # Atualização do faturamento
            faturamento_total += calcular_total(
                venda["preco"],
                venda["quantidade"],
                venda["desconto"]
            )

        except (ValueError, TypeError) as erro:
            print(f"Erro ao processar {venda['nome']}: {erro}")

        except KeyError as erro:
            print(f"Campo obrigatório ausente: {erro}")

    print("\n===== RESUMO FINAL =====")
    print(f"Faturamento total: R$ {faturamento_total:.2f}")


# ==========================================================
# EXECUÇÃO PRINCIPAL
# ==========================================================

if __name__ == "__main__":
    executar_sistema()
