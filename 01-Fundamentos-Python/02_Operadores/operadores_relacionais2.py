x = y = z = False
n1 = n2 = 0


print ('digite um numero: ')
n1 = int (input())
n2 = int (input('Digite outro numero: '))

x = n1 == n2
print('são iguais? ', x, '\n')

z = n1 > n2
print(n1,'é maior que ', n2, '?', z, '\n')

y = n1 != n2
print('são diferentes? ' + str(y))