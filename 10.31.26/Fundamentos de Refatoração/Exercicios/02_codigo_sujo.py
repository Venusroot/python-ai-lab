
# Dados iniciais
valor_produto = 1500.00
percentual_desconto = 0.10

# Cálculo do desconto
valor_desconto = valor_produto * percentual_desconto

# Cálculo do valor final
valor_final = valor_produto - valor_desconto

# Exibição dos resultados
print("=== Cálculo de Desconto ===")
print(f"Valor original: R$ {valor_produto:.2f}")
print(f"Percentual de desconto: {percentual_desconto:.0%}")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")
