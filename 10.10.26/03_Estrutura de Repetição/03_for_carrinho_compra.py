carrinho_de_compras = [
    {"nome": "Teclado",         "preco": 150.00},
    {"nome": "Mouse",           "preco": 40.50},
    {"nome": "Monitor",         "preco": 950.00},
    {"nome": "Cadeira Gamer",   "preco": 500.00}
]

total_compra = 0.0

# Para cada 'produto' na lista 'carrinho_de_compras'...
for produto in carrinho_de_compras:
    # ...pegue o preço desse produto e soma ao total.
    preco_item = produto["preco"]
    total_compra += preco_item
    print(f"Adicionando {produto['nome']} (R$ {preco_item:.2f}) ao total.")

print("-" * 50)
# A formatação :.2f garante que o valor seja exibido com duas casas decimais.
print(f"O valor total da compra é: R$ {total_compra:.2f}")








































