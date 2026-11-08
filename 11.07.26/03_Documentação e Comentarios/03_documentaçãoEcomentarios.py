
def calcular_preco_com_desconto(valor_original, percentual_desconto):
    """
    Calcula o preço final de um produto após aplicar um desconto.

    Parâmetros:
        valor_original (float): preço original do produto.
        percentual_desconto (float): percentual de desconto aplicado.

    Retorno:
        float: preço final do produto com desconto.
    """

    # Calcula o valor correspondente ao desconto
    valor_desconto = valor_original * (percentual_desconto / 100)

    # Subtrai o desconto do valor original
    preco_final = valor_original - valor_desconto

    # Retorna o preço final com desconto
    return preco_final


# Exemplo de utilização
preco = 200.00
desconto = 15

resultado = calcular_preco_com_desconto(preco, desconto)

print(f"Preço original: R$ {preco:.2f}")
print(f"Desconto: {desconto}%")
print(f"Preço final: R$ {resultado:.2f}")
