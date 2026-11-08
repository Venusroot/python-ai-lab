# **B) Simulação de "Verificação e Justificativa"**

# Simulação: IA instruída a validar o conhecimento
bibliotecas_reais = ["pandas", "numpy", "scikit-learn"]

def ia_com_verificacao(biblioteca):
    print("--- Analisando base de conhecimento... ---")
    if biblioteca.lower() in bibliotecas_reais:
        return f"A biblioteca {biblioteca} é real e serve para análise de dados."
    else:
        # Instrução: "Se não souber, admita que não sabe"
        return "Erro: Não encontrei informações confirmadas sobre essa biblioteca. Não vou inventar dados."

print(f"\nIA com trava: {ia_com_verificacao('SuperPyData')}")

