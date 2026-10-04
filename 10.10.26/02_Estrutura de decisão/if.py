# Atribuindo um valor qualquer para a variável y
y = int(input('Digite um número inteiro: '))

# Utilizando o comando if para verificar se o número é maior que 2
if (y > 2):
    print('\nO número é maior que dois!\n')
    print('Podemos utilizar mais de um comando dentro de um único if')
    print(y, '+ 5 =', y+5)

# Lembrando que em python a identação é extremamente importante
print('\nEste print está fora do if e será executado independente da condição')

