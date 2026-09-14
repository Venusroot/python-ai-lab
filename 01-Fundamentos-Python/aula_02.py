nome = 'SENAI'
idade = 30
altura = 1.70

print("Nome: %s, Idade: %d, Altura: %s" %(nome, idade, altura))

# %d = Decimal Inteiro 
# %s = String
# O "%" à esqueda é o operador da formatação 

# Usadndo o f-string
print(f'Nome: {nome}, Idade: {idade}, Altura: {altura:.2f}')

# Usando o metodo format()
print('Nome: {}, Idade: {}'.format(nome,idade))

