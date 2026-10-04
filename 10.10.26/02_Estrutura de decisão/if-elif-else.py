
# Atribuindo um valor a idade
idade = int(input("Digite sua idade: "))

# Verificando se o usuário é uma criança
if(idade <= 15):
    print('\nVocê é uma criança!')

# Verificando se o usuário é um adolescente
elif(idade > 15 and idade <= 18):
    print('\nVocê é um adolescente!')

# Verificando se o usuário é um adulto
elif(idade > 18 and idade <= 65):
    print('\nVocê é um adulto!')

# Verificando se o usuário é um idoso
else:
    print('\nVocê é um idoso!')

# Perceba que no último utilizamos o comando else, já que se as outras
# condições não forem satisfeita, o usuário só pode ser um idoso
