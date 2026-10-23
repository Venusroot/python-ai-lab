from func_biblioteca import soma, sub, mult, div, expo, imprimirResultado
# Acima mostra como importa as funções, posso usar também '*' pois ele já puxaria tudo para aqui.

def main():
    
    num1 = int(input("Digite primeiro numero: "))
    num2 = int(input("Digite segundo numero: "))
    operacao = input("Digite a operacao a ser calculada ( +, -, *, /, **): ")
    
    if operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/' or operacao == '**':
        if operacao == '+':
            res = soma(num1, num2)
        elif operacao == '-':
            res = sub(num1, num2)
        elif operacao == '*':
            res = mult(num1, num2)
        elif operacao == '/':
            res = div(num1, num2)
        elif operacao == '**':
            res = mult(num1, num2)
        imprimirResultado(res)
    else:
        print("Operação Invalida")
    
if __name__ == "__main__":
    main()
