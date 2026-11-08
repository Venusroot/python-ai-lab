
# ==========================================================
# SIMULADOR DE IA GENERATIVA - PYTHON + TKINTER
# ==========================================================

import tkinter as tk
from tkinter import ttk
import random
import re
from collections import defaultdict

# ==========================================================
# 1. MEMÓRIA TREINADA
# ==========================================================

memoria_treinada = {

    "Inteligência Artificial": [
        "A Inteligência Artificial é uma tecnologia que permite às máquinas aprender padrões e executar tarefas inteligentes.",
        "A Inteligência Artificial utiliza algoritmos para analisar dados, identificar padrões e produzir resultados.",
        "A IA está transformando a educação, a indústria, a saúde e diversos setores da sociedade.",
        "A Inteligência Artificial auxilia pessoas na resolução de problemas e na tomada de decisões."
    ],

    "IA Generativa": [
        "A IA Generativa é capaz de criar textos, imagens, códigos e conteúdos a partir de instruções humanas.",
        "A Inteligência Artificial Generativa utiliza modelos treinados para produzir novos conteúdos.",
        "A IA Generativa transforma informações aprendidas em respostas criativas e contextualizadas.",
        "Os modelos generativos produzem conteúdos diferentes conforme as instruções recebidas."
    ],

    "ChatGPT e LLM": [
        "O ChatGPT utiliza modelos de linguagem para interpretar perguntas e produzir respostas contextualizadas.",
        "LLM significa Large Language Model ou Grande Modelo de Linguagem.",
        "Os modelos LLM aprendem padrões linguísticos por meio do treinamento com grandes volumes de dados.",
        "Um modelo de linguagem utiliza probabilidades para prever sequências de palavras."
    ],

    "Programação Python": [
        "Python é uma linguagem de programação simples, versátil e utilizada no desenvolvimento de Inteligência Artificial.",
        "Python permite desenvolver aplicações, automatizar tarefas, analisar dados e criar sistemas inteligentes.",
        "A programação Python utiliza variáveis, funções, estruturas condicionais e estruturas de repetição.",
        "Python é uma excelente linguagem para estudantes que desejam aprender programação."
    ],

    "Educação e SENAI": [
        "O SENAI oferece educação profissional e tecnológica preparando estudantes para o mercado de trabalho.",
        "A educação tecnológica incentiva a inovação e o desenvolvimento de competências profissionais.",
        "Os estudantes podem utilizar Python para desenvolver projetos de Inteligência Artificial.",
        "A aprendizagem prática contribui para a formação de profissionais preparados para a indústria."
    ],

    "Tecnologia e Inovação": [
        "A tecnologia promove inovação, produtividade e novas oportunidades de aprendizagem.",
        "A transformação digital modifica a maneira como as empresas trabalham e se comunicam.",
        "A automação utiliza recursos tecnológicos para otimizar processos e melhorar resultados.",
        "A inovação tecnológica contribui para o desenvolvimento da sociedade."
    ]
}

# ==========================================================
# 2. TIPOS DE CONTEÚDO
# ==========================================================

tipos_conteudo = {
    "Explicação": "Explique o assunto de maneira didática, clara e detalhada.",
    "Exemplos": "Apresente exemplos práticos relacionados ao assunto.",
    "Resumo": "Produza um resumo com os principais conceitos do assunto.",
    "Aplicações": "Apresente aplicações práticas e situações do mundo real.",
    "Curiosidades": "Apresente curiosidades e informações interessantes."
}

# ==========================================================
# 3. MODELO DE PREDIÇÃO
# ==========================================================

modelo_palavras = defaultdict(list)

for categoria, textos in memoria_treinada.items():

    for texto in textos:

        palavras = re.findall(r"\w+|[.,!?;:]", texto)

        for i in range(len(palavras) - 1):

            atual = palavras[i].lower()
            proxima = palavras[i + 1]

            modelo_palavras[atual].append(proxima)


# ==========================================================
# 4. FUNÇÃO DE GERAÇÃO
# ==========================================================

def gerar_conteudo():

    contexto = combo_contexto.get()
    tipo = combo_tipo.get()
    tamanho = combo_tamanho.get()

    if not contexto:
        return

    textos = memoria_treinada[contexto]

    # Seleciona uma informação da memória
    resposta = random.choice(textos)

    # Complementa a resposta de acordo com o tipo escolhido
    complemento = tipos_conteudo[tipo]

    if tipo == "Exemplos":
        resposta += "\n\nExemplo prático: " + random.choice(textos)

    elif tipo == "Resumo":
        resposta = "RESUMO:\n" + resposta

    elif tipo == "Aplicações":
        resposta += "\n\nAplicação prática: " + random.choice(textos)

    elif tipo == "Curiosidades":
        resposta += "\n\nInformação adicional: " + random.choice(textos)

    else:
        resposta = "EXPLICAÇÃO:\n" + resposta

    # Ajusta o tamanho da resposta
    if tamanho == "Curto":
        resposta = resposta[:250]

    elif tamanho == "Médio":
        resposta = resposta[:500]

    else:
        resposta += "\n\n" + random.choice(textos)
        resposta += "\n\n" + random.choice(textos)

    # Exibe o resultado
    campo_saida.config(state="normal")
    campo_saida.delete("1.0", tk.END)
    campo_saida.insert(tk.END, resposta)
    campo_saida.config(state="disabled")

    status.config(
        text=f"Conteúdo gerado | Contexto: {contexto}"
    )


# ==========================================================
# 5. MOSTRAR MEMÓRIA TREINADA
# ==========================================================

def mostrar_memoria():

    contexto = combo_contexto.get()

    if not contexto:
        return

    campo_saida.config(state="normal")
    campo_saida.delete("1.0", tk.END)

    campo_saida.insert(
        tk.END,
        f"MEMÓRIA TREINADA: {contexto}\n\n"
    )

    for numero, texto in enumerate(
        memoria_treinada[contexto], start=1
    ):
        campo_saida.insert(
            tk.END,
            f"{numero}. {texto}\n\n"
        )

    campo_saida.config(state="disabled")

    status.config(text="Exibindo informações do treinamento.")


# ==========================================================
# 6. EXIBIR TODOS OS CONTEXTOS
# ==========================================================

def mostrar_contextos():

    campo_saida.config(state="normal")
    campo_saida.delete("1.0", tk.END)

    campo_saida.insert(tk.END, "CONTEXTOS DISPONÍVEIS\n\n")

    for categoria, textos in memoria_treinada.items():

        campo_saida.insert(tk.END, f"📚 {categoria}\n")

        for texto in textos:
            campo_saida.insert(tk.END, f"   • {texto}\n")

        campo_saida.insert(tk.END, "\n")

    campo_saida.config(state="disabled")

    status.config(text="Exibindo todos os contextos treinados.")


# ==========================================================
# 7. LIMPAR RESULTADO
# ==========================================================

def limpar():

    campo_saida.config(state="normal")
    campo_saida.delete("1.0", tk.END)
    campo_saida.config(state="disabled")

    status.config(text="Aguardando nova geração de conteúdo.")


# ==========================================================
# 8. INTERFACE GRÁFICA
# ==========================================================

janela = tk.Tk()

janela.title("Simulador de IA Generativa")
janela.geometry("900x700")
janela.minsize(750, 600)
janela.configure(bg="#F0F4F8")

# Estilo
estilo = ttk.Style()
estilo.theme_use("clam")

estilo.configure(
    "TCombobox",
    padding=7,
    font=("Arial", 11)
)

# Cabeçalho
cabecalho = tk.Frame(
    janela,
    bg="#07356B",
    height=100
)
cabecalho.pack(fill="x")

tk.Label(
    cabecalho,
    text="🤖 SIMULADOR DE IA GENERATIVA",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#07356B"
).pack(pady=(18, 5))

tk.Label(
    cabecalho,
    text="Predição de palavras e geração de conteúdo",
    font=("Arial", 11),
    fg="#DCE8F5",
    bg="#07356B"
).pack()

# Painel principal
painel = tk.Frame(
    janela,
    bg="#F0F4F8",
    padx=25,
    pady=15
)
painel.pack(fill="both", expand=True)

# Contexto
tk.Label(
    painel,
    text="1. SELECIONE O CONTEXTO",
    font=("Arial", 11, "bold"),
    bg="#F0F4F8",
    fg="#07356B"
).pack(anchor="w", pady=(5, 5))

combo_contexto = ttk.Combobox(
    painel,
    values=list(memoria_treinada.keys()),
    state="readonly",
    font=("Arial", 11)
)
combo_contexto.pack(fill="x", pady=(0, 15))
combo_contexto.current(0)

# Tipo de conteúdo
tk.Label(
    painel,
    text="2. TIPO DE CONTEÚDO",
    font=("Arial", 11, "bold"),
    bg="#F0F4F8",
    fg="#07356B"
).pack(anchor="w", pady=5)

combo_tipo = ttk.Combobox(
    painel,
    values=list(tipos_conteudo.keys()),
    state="readonly",
    font=("Arial", 11)
)
combo_tipo.pack(fill="x", pady=(0, 15))
combo_tipo.current(0)

# Tamanho
tk.Label(
    painel,
    text="3. TAMANHO DA RESPOSTA",
    font=("Arial", 11, "bold"),
    bg="#F0F4F8",
    fg="#07356B"
).pack(anchor="w", pady=5)

combo_tamanho = ttk.Combobox(
    painel,
    values=["Curto", "Médio", "Longo"],
    state="readonly",
    font=("Arial", 11)
)
combo_tamanho.pack(fill="x", pady=(0, 15))
combo_tamanho.current(1)

# Botões
botoes = tk.Frame(painel, bg="#F0F4F8")
botoes.pack(fill="x", pady=10)

def criar_botao(texto, comando, cor):

    return tk.Button(
        botoes,
        text=texto,
        command=comando,
        bg=cor,
        fg="white",
        font=("Arial", 10, "bold"),
        relief="flat",
        padx=12,
        pady=11,
        cursor="hand2"
    )

criar_botao(
    "✨ GERAR CONTEÚDO",
    gerar_conteudo,
    "#0755A5"
).pack(side="left", padx=4, expand=True, fill="x")

criar_botao(
    "📚 VER MEMÓRIA",
    mostrar_memoria,
    "#16805D"
).pack(side="left", padx=4, expand=True, fill="x")

criar_botao(
    "📖 CONTEXTOS",
    mostrar_contextos,
    "#6B4DA0"
).pack(side="left", padx=4, expand=True, fill="x")

criar_botao(
    "🗑 LIMPAR",
    limpar,
    "#D1495B"
).pack(side="left", padx=4, expand=True, fill="x")

# Área de saída
tk.Label(
    painel,
    text="4. SAÍDA GENERATIVA",
    font=("Arial", 11, "bold"),
    bg="#F0F4F8",
    fg="#07356B"
).pack(anchor="w", pady=(15, 5))

campo_saida = tk.Text(
    painel,
    height=12,
    font=("Arial", 11),
    wrap="word",
    bg="white",
    fg="#203047",
    padx=12,
    pady=12,
    relief="solid",
    borderwidth=1
)

campo_saida.pack(fill="both", expand=True)

campo_saida.insert(
    tk.END,
    "Selecione um contexto e clique em GERAR CONTEÚDO."
)

campo_saida.config(state="disabled")

# Rodapé / Status
status = tk.Label(
    janela,
    text="Sistema iniciado | Aguardando interação",
    font=("Arial", 9),
    bg="#DCE6F1",
    fg="#07356B",
    anchor="w",
    padx=15,
    pady=9
)

status.pack(fill="x")

# Executar
janela.mainloop()
