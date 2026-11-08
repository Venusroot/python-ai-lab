# **Simulador de Janela de Contexto (Memória)**
# Este script ilustra o que acontece quando uma conversa fica longa demais e a IA começa a "esquecer" o início.


# Janela de Contexto: Limite de 5 tokens de memória
janela_contexto = []
LIMITE_MEMORIA = 5

def adicionar_ao_chat(nova_mensagem):
    global janela_contexto
    # Adiciona a nova mensagem à memória
    janela_contexto.append(nova_mensagem)
    
    # Se ultrapassar o limite, a IA "esquece" o token mais antigo
    if len(janela_contexto) > LIMITE_MEMORIA:
        esquecido = janela_contexto.pop(0)
        print(f"--- [AVISO]: A IA esqueceu o token: '{esquecido}' ---")
    
    print(f"Memória atual da IA: {janela_contexto}")

# Simulação de conversa
mensagens = ["Olá", "Tudo bem?", "Como programar?", "Use Python", "E o Pandas?", "O que eu perguntei primeiro?"]
for msg in mensagens:
    print(f"\nUsuário diz: {msg}")
    adicionar_ao_chat(msg)

