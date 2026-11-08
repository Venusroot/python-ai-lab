
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# ==========================================
# CONFIGURACAO
# ==========================================

BG = "#101C36"
AZUL = "#2563EB"
SIDEBAR = "#172554"
BRANCO = "#FFFFFF"

janela = tk.Tk()
janela.title("Laboratório de IA Generativa")
janela.geometry("1150x750")
janela.minsize(900, 600)
janela.configure(bg=BG)

contexto_atual = ""

# ==========================================
# FUNCOES GERAIS
# ==========================================

def limpar_tela():
    for widget in area_principal.winfo_children():
        widget.destroy()


def atualizar_status(mensagem):
    status.config(text=mensagem)


def sobre():
    messagebox.showinfo(
        "Sobre o sistema",
        "Laboratório de IA Generativa\n"
        "Simulador educacional de LLM\n"
        "Desenvolvido em Python e Tkinter."
    )


def sair():
    if messagebox.askyesno(
        "Sair",
        "Deseja encerrar o sistema?"
    ):
        janela.destroy()


# ==========================================
# TELA INICIAL
# ==========================================

def tela_inicial():

    limpar_tela()

    tk.Label(
        area_principal,
        text="LABORATÓRIO DE IA GENERATIVA",
        font=("Arial", 23, "bold"),
        bg="white",
        fg=SIDEBAR
    ).pack(pady=30)

    tk.Label(
        area_principal,
        text="Bem-vindo ao ambiente de simulação de LLM",
        font=("Arial", 13),
        bg="white",
        fg="#64748B"
    ).pack(pady=10)

    painel = tk.Frame(
        area_principal,
        bg="#EFF6FF",
        padx=30,
        pady=25
    )
    painel.pack(padx=40, pady=30, fill="x")

    tk.Label(
        painel,
        text="Escolha uma opção no menu lateral:",
        font=("Arial", 13, "bold"),
        bg="#EFF6FF",
        fg=SIDEBAR
    ).pack(anchor="w", pady=10)

    tk.Label(
        painel,
        text="1. Configure o contexto da IA.\n\n"
             "2. Organize a base de conhecimento.\n\n"
             "3. Simule a predição de palavras.\n\n"
             "4. Analise os resultados gerados.",
        justify="left",
        font=("Arial", 12),
        bg="#EFF6FF",
        fg="#334155"
    ).pack(anchor="w")


# ==========================================
# GERADOR DE CONTEXTO
# ==========================================

def tela_contexto():

    limpar_tela()

    tk.Label(
        area_principal,
        text="GERADOR DE CONTEXTO",
        font=("Arial", 20, "bold"),
        bg="white",
        fg=SIDEBAR
    ).pack(pady=15)

    formulario = tk.Frame(
        area_principal,
        bg="white",
        padx=30
    )
    formulario.pack(fill="both", expand=True)

    def rotulo(texto):
        tk.Label(
            formulario,
            text=texto,
            bg="white",
            fg="#334155",
            font=("Arial", 10, "bold")
        ).pack(anchor="w", pady=(8, 2))

    def combo(opcoes, padrao):
        campo = ttk.Combobox(
            formulario,
            values=opcoes,
            state="readonly"
        )
        campo.set(padrao)
        campo.pack(fill="x", pady=3)
        return campo

    rotulo("Tema principal")
    tema = combo([
        "Inteligência Artificial",
        "Python",
        "Robótica",
        "Indústria 4.0",
        "Automação Industrial",
        "Machine Learning",
        "Ciência de Dados"
    ], "Inteligência Artificial")

    rotulo("Tipo de conteúdo")
    tipo = combo([
        "Texto explicativo",
        "Artigo técnico",
        "Resumo",
        "Tutorial",
        "Perguntas e respostas",
        "Exemplo de código",
        "Estudo de caso",
        "Questionário",
        "História educativa"
    ], "Texto explicativo")

    rotulo("Tamanho da resposta")
    tamanho = combo([
        "Muito curta",
        "Curta",
        "Média",
        "Longa",
        "Muito longa"
    ], "Média")

    rotulo("Nível de complexidade")
    nivel = combo([
        "Básico",
        "Intermediário",
        "Avançado",
        "Especialista"
    ], "Intermediário")

    rotulo("Estilo de linguagem")
    estilo = combo([
        "Didático",
        "Técnico",
        "Formal",
        "Informal",
        "Acadêmico",
        "Criativo"
    ], "Didático")

    rotulo("Público-alvo")
    publico = combo([
        "Estudantes",
        "Professores",
        "Programadores",
        "Profissionais da indústria",
        "Iniciantes",
        "Público geral"
    ], "Estudantes")

    rotulo("Palavras-chave")
    palavras = tk.Entry(formulario)
    palavras.pack(fill="x", pady=3)

    rotulo("Objetivo e instruções adicionais")
    objetivo = tk.Text(
        formulario,
        height=4,
        font=("Arial", 10)
    )
    objetivo.pack(fill="x", pady=5)

    def gerar():

        global contexto_atual

        contexto_atual = f"""
CONFIGURAÇÃO DO CONTEXTO

Tema: {tema.get()}
Tipo de conteúdo: {tipo.get()}
Tamanho: {tamanho.get()}
Complexidade: {nivel.get()}
Estilo: {estilo.get()}
Público-alvo: {publico.get()}
Palavras-chave: {palavras.get()}

Objetivo e instruções:
{objetivo.get("1.0", tk.END).strip()}

INSTRUÇÃO PARA GERAÇÃO:
Produza conteúdo sobre {tema.get()},
no formato {tipo.get()},
com tamanho {tamanho.get()},
complexidade {nivel.get()},
linguagem {estilo.get()},
adequado para {publico.get()}.

Utilize as palavras-chave informadas,
respeitando o objetivo e as instruções.
"""

        messagebox.showinfo(
            "Sucesso",
            "Contexto configurado!"
        )

        tela_visualizar()

    tk.Button(
        formulario,
        text="GERAR CONTEXTO",
        bg=AZUL,
        fg="white",
        font=("Arial", 10, "bold"),
        command=gerar,
        pady=9
    ).pack(fill="x", pady=15)


# ==========================================
# VISUALIZAR CONTEXTO
# ==========================================

def tela_visualizar():

    limpar_tela()

    tk.Label(
        area_principal,
        text="CONTEXTO GERADO",
        font=("Arial", 20, "bold"),
        bg="white",
        fg=SIDEBAR
    ).pack(pady=15)

    texto = tk.Text(
        area_principal,
        font=("Consolas", 11),
        wrap="word",
        padx=15,
        pady=15
    )
    texto.pack(fill="both", expand=True, padx=25, pady=10)

    texto.insert("1.0", contexto_atual)

    botoes = tk.Frame(area_principal, bg="white")
    botoes.pack(pady=10)

    def copiar():
        janela.clipboard_clear()
        janela.clipboard_append(
            texto.get("1.0", tk.END)
        )
        atualizar_status("Contexto copiado.")

    def salvar():
        arquivo = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Texto", "*.txt")]
        )

        if arquivo:
            with open(arquivo, "w", encoding="utf-8") as f:
                f.write(texto.get("1.0", tk.END))

            atualizar_status("Arquivo salvo.")

    tk.Button(
        botoes,
        text="COPIAR",
        bg="#16A34A",
        fg="white",
        command=copiar
    ).pack(side="left", padx=5)

    tk.Button(
        botoes,
        text="SALVAR TXT",
        bg=AZUL,
        fg="white",
        command=salvar
    ).pack(side="left", padx=5)


# ==========================================
# BASE DE CONHECIMENTO
# ==========================================

def tela_base():

    limpar_tela()

    tk.Label(
        area_principal,
        text="BASE DE CONHECIMENTO",
        font=("Arial", 20, "bold"),
        bg="white",
        fg=SIDEBAR
    ).pack(pady=20)

    texto = tk.Text(
        area_principal,
        font=("Consolas", 11),
        wrap="word"
    )
    texto.pack(fill="both", expand=True, padx=25, pady=15)

    texto.insert(
        "1.0",
        "Exemplo de estrutura de treinamento:\n\n"
        'memoria_treinada = {\n'
        '    "O": ["ChatGPT", "Python", "SENAI"],\n'
        '    "ChatGPT": ["é", "utiliza", "representa"],\n'
        '    "é": ["uma inteligência artificial"],\n'
        '    "Python": ["é", "permite", "facilita"]\n'
        '}\n'
    )

    atualizar_status("Base de conhecimento.")


# ==========================================
# SIMULADOR DE PREDICAO
# ==========================================

def tela_simulador():

    limpar_tela()

    tk.Label(
        area_principal,
        text="SIMULADOR DE PREDIÇÃO",
        font=("Arial", 20, "bold"),
        bg="white",
        fg=SIDEBAR
    ).pack(pady=20)

    tk.Label(
        area_principal,
        text="Digite uma palavra inicial:",
        bg="white"
    ).pack()

    entrada = tk.Entry(
        area_principal,
        font=("Arial", 13)
    )
    entrada.pack(pady=10)

    resultado = tk.Text(
        area_principal,
        height=10,
        font=("Arial", 12),
        wrap="word"
    )
    resultado.pack(fill="both", expand=True, padx=30, pady=15)

    import random

    memoria = {
        "O": ["ChatGPT", "Python", "SENAI"],
        "ChatGPT": ["é", "utiliza", "representa"],
        "é": ["uma inteligência artificial", "uma ferramenta"],
        "Python": ["é", "permite", "facilita"],
        "SENAI": ["oferece", "ensina", "desenvolve"]
    }

    def prever():

        palavra = entrada.get().strip()

        if not palavra:
            return

        frase = [palavra]

        for i in range(5):

            if palavra not in memoria:
                break

            palavra = random.choice(memoria[palavra])
            frase.append(palavra)

        resultado.delete("1.0", tk.END)
        resultado.insert(
            tk.END,
            "Saída generativa:\n\n" + " ".join(frase)
        )

    tk.Button(
        area_principal,
        text="GERAR PREDIÇÃO",
        bg=AZUL,
        fg="white",
        command=prever,
        pady=8
    ).pack(pady=5)


# ==========================================
# MENU SUPERIOR
# ==========================================

barra_menu = tk.Menu(janela)

# Arquivo
menu_arquivo = tk.Menu(barra_menu, tearoff=0)
menu_arquivo.add_command(
    label="Novo contexto",
    command=tela_contexto
)
menu_arquivo.add_command(
    label="Visualizar contexto",
    command=tela_visualizar
)
menu_arquivo.add_separator()
menu_arquivo.add_command(
    label="Sair",
    command=sair
)

barra_menu.add_cascade(
    label="Arquivo",
    menu=menu_arquivo
)

# Configuracoes
menu_config = tk.Menu(barra_menu, tearoff=0)
menu_config.add_command(
    label="Gerar contexto",
    command=tela_contexto
)
menu_config.add_command(
    label="Base de conhecimento",
    command=tela_base
)

barra_menu.add_cascade(
    label="Configurações",
    menu=menu_config
)

# Treinamento
menu_treinamento = tk.Menu(barra_menu, tearoff=0)
menu_treinamento.add_command(
    label="Base de conhecimento",
    command=tela_base
)
barra_menu.add_cascade(
    label="Treinamento",
    menu=menu_treinamento
)

# Simulador
menu_simulador = tk.Menu(barra_menu, tearoff=0)
menu_simulador.add_command(
    label="Predição de palavras",
    command=tela_simulador
)
barra_menu.add_cascade(
    label="Simulador",
    menu=menu_simulador
)

# Relatorios
menu_relatorios = tk.Menu(barra_menu, tearoff=0)
menu_relatorios.add_command(
    label="Visualizar contexto",
    command=tela_visualizar
)
barra_menu.add_cascade(
    label="Relatórios",
    menu=menu_relatorios
)

# Ajuda
menu_ajuda = tk.Menu(barra_menu, tearoff=0)
menu_ajuda.add_command(
    label="Sobre",
    command=sobre
)
barra_menu.add_cascade(
    label="Ajuda",
    menu=menu_ajuda
)

janela.config(menu=barra_menu)


# ==========================================
# MENU LATERAL
# ==========================================

estrutura = tk.Frame(janela, bg=BG)
estrutura.pack(fill="both", expand=True)

menu_lateral = tk.Frame(
    estrutura,
    bg=SIDEBAR,
    width=220
)
menu_lateral.pack(side="left", fill="y")
menu_lateral.pack_propagate(False)

tk.Label(
    menu_lateral,
    text="NAVEGAÇÃO",
    bg=SIDEBAR,
    fg="#93C5FD",
    font=("Arial", 12, "bold")
).pack(pady=20)


def botao_menu(texto, comando):

    tk.Button(
        menu_lateral,
        text=texto,
        command=comando,
        bg=SIDEBAR,
        fg="white",
        activebackground=AZUL,
        activeforeground="white",
        font=("Arial", 10),
        relief="flat",
        anchor="w",
        padx=20,
        pady=12
    ).pack(fill="x")


botao_menu("Painel inicial", tela_inicial)
botao_menu("Gerar contexto", tela_contexto)
botao_menu("Base de conhecimento", tela_base)
botao_menu("Predição de palavras", tela_simulador)
botao_menu("Visualizar contexto", tela_visualizar)
botao_menu("Sobre o sistema", sobre)


# ==========================================
# AREA DE TRABALHO
# ==========================================

area_principal = tk.Frame(
    estrutura,
    bg="white"
)

area_principal.pack(
    side="right",
    fill="both",
    expand=True
)


# ==========================================
# BARRA DE STATUS
# ==========================================

status = tk.Label(
    janela,
    text="Sistema iniciado.",
    bg="#E2E8F0",
    fg="#4E420A",
    anchor="w",
    padx=10
)

status.pack(fill="x", side="bottom")


# ==========================================
# INICIALIZACAO
# ==========================================

tela_inicial()

janela.mainloop()
