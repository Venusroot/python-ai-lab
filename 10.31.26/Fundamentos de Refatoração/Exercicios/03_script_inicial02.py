def calcular_desconto(valor, percentual_desconto):
    """
    Calcula o valor final após aplicar um desconto.
    """

    if valor < 0:
        raise ValueError("O valor não pode ser negativo.")

    if not 0 <= percentual_desconto <= 100:
        raise ValueError("O desconto deve estar entre 0 e 100%.")

    valor_desconto = valor * (percentual_desconto / 100)
    valor_final = valor - valor_desconto

    return round(valor_final, 2)


# Entrada de dados do usuário
try:
    valor = float(input("Digite o valor do produto: R$ "))
    percentual = float(input("Digite o percentual de desconto: "))

    # Chamada da função
    resultado = calcular_desconto(valor, percentual)

    # Exibição do resultado
    print("\n===== RESULTADO =====")
    print(f"Valor original: R$ {valor:.2f}")
    print(f"Desconto aplicado: {percentual:.2f}%")
    print(f"Valor final: R$ {resultado:.2f}")

except ValueError as erro:
    print(f"Erro: {erro}")