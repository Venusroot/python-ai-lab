def ler_nota(numero):
    while True:
        nota = input(f"Digite a Nota {numero:02d}: ")

        # Aceita somente números inteiros
        if not nota.isdigit():
            print("Erro: digite apenas números inteiros de 0 a 100.")
            continue

        nota = float(nota)

        # Verifica o intervalo permitido
        if 0 <= nota <= 100:
            return nota

        print("-------Erro: a nota deve estar entre 0 e 100.-------")


def main():
    # Recebe o nome do aluno
    aluno = input("\nDigite o nome do aluno: ").strip()

    # Recebe as três notas
    n1 = ler_nota(1)
    n2 = ler_nota(2)
    n3 = ler_nota(3)

    # Calcula a média
    media = (n1 + n2 + n3) / 3

    # Exibe os resultados
    print(f"\nAluno: {aluno}")
    print(f"Média final: {media:.2f}")

    # Verifica a situação do aluno
    if media >= 70:
        print(f"\nParabéns, {aluno}! Você foi aprovado(a)!")

    elif media >= 40:
        print(f"\n{aluno} está de recuperação.")
        print("\nVocê terá que fazer o exame final.")

    else:
        print(f"{aluno}, infelizmente você está reprovado(a).")


# Executa o programa
if __name__ == "__main__":
    main()
