# Phyton é uma linguagem  NAO TIPADA, isto é, não utiliza o tipo
# (string, int, float, booleano) quando cria a variavel

# variaveis -> espaço dentro da memoria RAM para guardar dados/informações

# Nomes de variaveis:
# - não podem começar com numeros => 1num = 20 (erro!) -> num1 = 20 (ok)
# - não podem ter caracteres especiais: preço (ç) -> preco
# - não podem ter espaços (valor carro), quando necessário 
# - utilizar o _ (underscroll ou underline) -> valor_carro / valorCarro
# - colocar nome significativos para variaveis
# - as variaveis em Python são Case Sensitive: python, PYTHON, pyTHON 
# -----------------------------------------------------------------------
# def main():  
# ->Define um bloco de código organizado como a 
#    lógica principal do script (por convenção).
#
#if __name__ == "__main__":  
# ->Verifica se o script está sendo executado diretamente.
#
# A chamada main() 
#  -> dentro do if executa a lógica principal definida em 
#     def main(): apenas quando o script é executado diretamente.
# -----------------------------------------------------------------------

def main():

    # variavies do tipo inteiro ( numero inteirs: 0, 1, 2, -9, 22222)
    idade = 32
    numero_de_alunos = 15
    numeroAlunos = 16

    # Case Sensitive
    python = 0
    Python = 0
    PYTHON = 0

    # Variaiveis do Tipo Real ( Numeros Reais / Ponto Flutuante: 1.2 , 7.98)
    altura = 1.74
    precoPruduto = 19.99
    largura = 15.0

    # Variaiveis do tipo String (Palavras, Frases, Letras, Caracterres)
    # - devem estar entre aspas duplas ou simples
    nome = "Alice"
    mensagem = "Olá, seja bem-vindo!"
    endereco = 'Rua das Flores, 123' 

    # Variáveis do Tipo Booleano (true ou false)
    is_python_fun = True
    hoje_esta_chovendo = False

    print ("A idade de José é: ",idade)
    print ("O valor da altura é: ",altura)
    print ("Hoje esta chovendo? ", hoje_esta_chovendo)

    print ("Olá ",nome, "! Você tem ", idade, "anos.")
    print (f"Olá {nome} ! Você tem {idade} anos.")

# Fechamento da tag main
if __name__=="__main__":
    main()