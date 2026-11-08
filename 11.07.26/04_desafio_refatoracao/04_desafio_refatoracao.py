### **Desafio de Refatoração: O Sistema de Vendas **

# * Este exercício simula um "código legado" (antigo e mal escrito) de um sistema de vendas. 
#   Ele contém **erros de sintaxe** (que impedem a execução), **erros de lógica** (que geram resultados errados) 
#   e **má estruturação** (que dificulta a manutenção).

# **Código "Sujo":**
# python

# SCRIPT COM ERROS - NÃO EXECUTAR DIRETAMENTE
def Calc(p, q, d)
    # Erro de lógica: desconto aplicado de forma estranha
    res = p * q - d
    return res

vendas = [["Mouse", 50, 2, 10], ["Teclado", 150, 1, "5"], ["Monitor", 800, 0, 0]]

for v in vendas:
    # Erro de sintaxe: falta de dois pontos e indentação
    # Erro de lógica: o sistema quebra se a quantidade for 0 (divisão por zero oculta)
    nome = v
    pre = v
    qtd = v
    desc = v
    
    total = Calc(pre, qtd, desc)
    
    print("Produto: " + nome + " | Total: " + str(total))
    
    # Verificação de estoque mal feita
    media = pre / qtd
    print("Preço médio por item: " + str(media))


# **Instrução:** 
#  O script acima deveria calcular o faturamento de uma loja, 
#  aplicar descontos e verificar o estoque. 
#  No entanto, ele está cheio de erros e é impossível de ler. 
#  Seu objetivo é usar a IA para:
# 1. Identificar e corrigir os erros de sintaxe e lógica.
# 2. Refatorar o código aplicando as boas práticas de **Clean Code** e **PEP8**.
# 3. Implementar tratamento de erros com `try/except`.
# 4. Gerar a documentação técnica (**Docstrings**).


