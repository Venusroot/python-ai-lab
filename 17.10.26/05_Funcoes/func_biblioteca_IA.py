
# func_biblioteca.py

def soma(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def div(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")

    return num1 / num2


def expo(num1, num2):
    return num1 ** num2


def imprimirResultado(res):
    print(f"\nResultado: {res:g}")
