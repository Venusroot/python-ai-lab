# **A) Simulação de Análise de Arquivo (Lógica Python)**
# Embora a análise ocorra na interface, o desenvolvedor precisa entender como a IA "pensa" ao ler um arquivo. Este script simula o envio de um "log de erro" para a IA.


# Simulação: O que o aluno envia (via captura de tela ou arquivo txt)
log_erro = """
File "script.py", line 15
    print("Resultado:", resultado)
SyntaxError: invalid syntax
"""

# Prompt Estruturado para a Interface (Dica Prática):
prompt_debug = f"""
Analise esta captura de tela do meu terminal (texto abaixo):
{log_erro}
1. Identifique o erro.
2. Explique por que aconteceu.
3. Forneça o código corrigido.
"""
print("Prompt sugerido para o ChatGPT:")
print(prompt_debug)
