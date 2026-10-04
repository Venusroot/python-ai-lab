# Estruturas de Repetição:
#   - Utilizada para repetir uma parte do código;
#   - Percorrer listas(arrays)

def main():

    # Repetir código - WHILE

    # 1. Repetir conforme uma quantidade de vezes, no caso, 10x
    i = 0
    while i < 10:
        print("Ola")
        i = i + 1   
        print(i) 
    # #     i += 1

# ===============================================================

    # 2. Repetir até o número ser diferente de 1
    # opcao = 1
    # while opcao == 1:
    #     opcao = int(input("Digite um numero diferente de 1 para terminar:"))

# ==================================================================

    # 3. Repetir até a nota valida
    # nota = int( input("Digite sua nota:") )

    # while nota < 0 or nota > 50:
    #     print("Sua nota deve estar entre 0 e 50, digite novamente")
    #     nota = int( input("Digite sua nota outra vez:") )

# =================================================================

    # # 4. Tabuada
    # multiplo = 5
    # incremento = 0

    # while incremento <= 10:
    #     resultado = multiplo * incremento

    #     print(f"{multiplo} x {incremento} = {resultado}")
    #     incremento += 1

# ============================================================


    # FOR
    # # 1. Repetir uma quantidade de vezes
    # for i in range(11):
    #     print(i)

    # for i in range(3,10):
    #     print(i)


    # for i in range(1,12,2):
    #     print(i)
    
    
# ==================================================================
    
    
    # frutas = ["pera", "uva", "maçã", "banana", "melancia", "laranja", "abacate", "abacaxi", "limão", "carambola"]
    
    # print(frutas[0])
    # print(frutas[1])
    # print(frutas[2])
    # print(frutas[3])

    # for i in range(10):
    #     #print(frutas[1])
        # print(f"{i+1} - {frutas[1]}")


    # for elemento in lista:
    # for fruta in frutas:
    #     print(fruta)

# =======================================================================

    # nomeAlunos = ["Lara", "Bia", "Luis","Juca","Manuela"]
    # tamanhoLista = len(nomeAlunos)
    # print(f"A lista tem {tamanhoLista} alunos")
    # for alunos in nomeAunos
    # print(alunos)

    # for i in range(len(nomeAlunos) ): # len é usada para retornar o número de itens de um objeto
    #     print(f'{i+1} - {nomeAlunos[i]}')





if __name__ == "__main__":
    main()