
# calculadora.py

from func_biblioteca_IA import soma, sub, mult, div, expo


def main():
    operacoes = {
        "1": ("Adição", "+", soma),
        "2": ("Subtração", "-", sub),
        "3": ("Multiplicação", "*", mult),
        "4": ("Divisão", "/", div),
        "5": ("Potenciação", "**", expo),
    }

    print("=" * 35)
    print("       CALCULADORA PYTHON")
    print("=" * 35)

    while True:
        print("\nEscolha uma operação:")
        print("1 - Adição (+)")
        print("2 - Subtração (-)")
        print("3 - Multiplicação (*)")
        print("4 - Divisão (/)")
        print("5 - Potenciação (**)")
        print("0 - Sair")

        opcao = input("\nDigite sua opção: ").strip()

        if opcao == "0":
            print("\nCalculadora encerrada. Até mais!")
            break

        if opcao not in operacoes:
            print("Opção inválida! Escolha uma opção de 0 a 5.")
            continue

        nome, simbolo, funcao = operacoes[opcao]

        try:
            num1 = float(
                input("Digite o primeiro número: ").replace(",", ".")
            )

            num2 = float(
                input("Digite o segundo número: ").replace(",", ".")
            )

            resultado = funcao(num1, num2)

            print(f"\nOperação: {nome}")
            print(
                f"{num1:g} {simbolo} {num2:g} = "
                f"{resultado:g}"
            )

        except ValueError:
            print(
                "Entrada inválida! Digite números válidos, "
                "como 10 ou 2.5."
            )

        except ZeroDivisionError as erro:
            print(f"Erro: {erro}")

        except OverflowError:
            print("Erro: o resultado é grande demais.")

        print("\n" + "-" * 35)


if __name__ == "__main__":
    main()
