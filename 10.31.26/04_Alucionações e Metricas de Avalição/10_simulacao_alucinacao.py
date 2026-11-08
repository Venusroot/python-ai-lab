# **A) Simulação de "Alucinação" (Sem Filtro de Segurança)**

# Simulação: IA tenta responder sobre uma biblioteca que não existe
def ia_sem_filtro(pergunta):
    # A IA "acha" que deve sempre responder algo
    return "A biblioteca 'SuperPyData' serve para teletransporte de arquivos."

pergunta = "Para que serve a biblioteca SuperPyData no Python?"
print(f"Usuário: {pergunta}")
print(f"IA (Alucinando): {ia_sem_filtro(pergunta)}")

