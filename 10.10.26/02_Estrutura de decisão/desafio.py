# Desenvolver um programa para verificar a situação do aluno
# em relação ao sua promoção escola
#   [ ] 1. O aluno deverá digitar 3 notas através do teclado
#   [ ] 2. Seu programa deverá calcular a média das notas
#   [ ] 3. A partir da média, verificar qual situação o aluno se
# encontra conforme notas abaixo:
#       3.1 nota > 70 - aprovado
#       3.2 nota < 40 - reprovado
#       3.3 nota entre 40 e 70 - exame/recuperação
#   [ ] 4. Não será permitido médias acima de 100 e abaixo de zero
#   [ ] 5. Caso isso ocorrá o aluno deverá ser informado sobre um erro
# de digitação
#   [ ] 6. Mostrar na tela para o aluno a situação final baseado na
# nota digitada.
# --------------------------------------------------------------------


aluno = (input(f"\nDigite o nome do aluno: "))
n1 = float(input("Digite a Nota 01: "))
n2 = float(input("Digite a Nota 02: "))
n3 = float(input("Digite a Nota 03: "))

media = (n1+n2+n3)/3

if (media > 100):
    print(f"\n{aluno} digitou alguma nota errada, tente novamente!")

elif(media >= 70):
    print(f"\nParabéns {aluno} você foi aprovado! Sua media final foi {media:.2f}")

elif (media >= 40):
    print(f"\n{aluno} está de recuperação, sua nota foi {media:.2f} terá que fazer o exame final")

else:
    print(f"\n{aluno} infelizmente você está reprovado! Sua media foi {media:.2f}")

    

