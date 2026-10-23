
import tkinter as tk
import ast
import operator
import math


# Operações permitidas
OPERADORES = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def calcular_expressao(no):
    """Calcula somente expressões matemáticas permitidas."""

    if isinstance(no, ast.Expression):
        return calcular_expressao(no.body)

    if isinstance(no, ast.Constant) and type(no.value) in (int, float):
        return no.value

    if isinstance(no, ast.BinOp) and type(no.op) in OPERADORES:
        esquerda = calcular_expressao(no.left)
        direita = calcular_expressao(no.right)

        # Evita cálculos que gerem números excessivamente grandes
        if isinstance(no.op, ast.Pow):
            if abs(direita) > 1000:
                raise ValueError("Expoente muito grande.")

        return OPERADORES[type(no.op)](esquerda, direita)

    if isinstance(no, ast.UnaryOp) and type(no.op) in OPERADORES:
        valor = calcular_expressao(no.operand)
        return OPERADORES[type(no.op)](valor)

    raise ValueError("Expressão inválida.")


def calcular():
    expressao = visor.get().replace(",", ".")

    try:
        arvore = ast.parse(expressao, mode="eval")
        resultado = calcular_expressao(arvore)

        if isinstance(resultado, complex):
            raise ValueError("Resultado complexo não suportado.")

        if isinstance(resultado, float) and not math.isfinite(resultado):
            raise ValueError("Resultado fora do limite numérico.")

        visor.delete(0, tk.END)
        visor.insert(0, str(resultado))

    except ZeroDivisionError:
        mostrar_erro("Não é possível dividir por zero.")

    except (ValueError, SyntaxError, OverflowError, TypeError):
        mostrar_erro("Operação inválida.")


def mostrar_erro(mensagem):
    visor.delete(0, tk.END)
    visor.insert(0, mensagem)


def adicionar(valor):
    atual = visor.get()

    if atual in (
        "Operação inválida.",
        "Não é possível dividir por zero.",
    ):
        visor.delete(0, tk.END)

    visor.insert(tk.END, valor)


def limpar():
    visor.delete(0, tk.END)


def apagar():
    atual = visor.get()
    visor.delete(0, tk.END)
    visor.insert(0, atual[:-1])


def raiz_quadrada():
    try:
        valor = float(visor.get().replace(",", "."))

        if valor < 0:
            raise ValueError

        resultado = math.sqrt(valor)
        visor.delete(0, tk.END)
        visor.insert(0, str(resultado))

    except (ValueError, OverflowError):
        mostrar_erro("Não é possível calcular a raiz.")


# Janela principal
janela = tk.Tk()
janela.title("Calculadora Python")
janela.geometry("340x465")
janela.resizable(False, False)
janela.configure(bg="#171923")

# Visor
visor = tk.Entry(
    janela,
    font=("Arial", 22),
    justify="right",
    bg="#252A38",
    fg="white",
    insertbackground="white",
    relief="flat",
    borderwidth=0
)
visor.pack(fill="x", padx=15, pady=(20, 15), ipady=18)

# Teclas
botoes = [
    ("AC", 0, 0, limpar, "#3B4252"),
    ("⌫", 0, 1, apagar, "#3B4252"),
    ("%", 0, 2, lambda: adicionar("%"), "#3B4252"),
    ("÷", 0, 3, lambda: adicionar("/"), "#D89504"),

    ("7", 1, 0, lambda: adicionar("7"), "#292F3E"),
    ("8", 1, 1, lambda: adicionar("8"), "#292F3E"),
    ("9", 1, 2, lambda: adicionar("9"), "#292F3E"),
    ("×", 1, 3, lambda: adicionar("*"), "#D89504"),

    ("4", 2, 0, lambda: adicionar("4"), "#292F3E"),
    ("5", 2, 1, lambda: adicionar("5"), "#292F3E"),
    ("6", 2, 2, lambda: adicionar("6"), "#292F3E"),
    ("−", 2, 3, lambda: adicionar("-"), "#D89504"),

    ("1", 3, 0, lambda: adicionar("1"), "#292F3E"),
    ("2", 3, 1, lambda: adicionar("2"), "#292F3E"),
    ("3", 3, 2, lambda: adicionar("3"), "#292F3E"),
    ("+", 3, 3, lambda: adicionar("+"), "#D89504"),

    ("√", 4, 0, raiz_quadrada, "#3B4252"),
    ("0", 4, 1, lambda: adicionar("0"), "#292F3E"),
    (",", 4, 2, lambda: adicionar("."), "#292F3E"),
    ("=", 4, 3, calcular, "#D89504"),
]

# Área dos botões
area = tk.Frame(janela, bg="#171923")
area.pack(fill="both", expand=True, padx=12, pady=(0, 12))

for coluna in range(4):
    area.columnconfigure(coluna, weight=1)

for linha in range(5):
    area.rowconfigure(linha, weight=1)

for texto, linha, coluna, comando, cor in botoes:
    botao = tk.Button(
        area,
        text=texto,
        command=comando,
        font=("Arial", 15, "bold"),
        bg=cor,
        fg="white",
        activebackground="#4A5568",
        activeforeground="white",
        relief="flat",
        borderwidth=0,
        cursor="hand2"
    )
    botao.grid(
        row=linha,
        column=coluna,
        sticky="nsew",
        padx=3,
        pady=3
    )

# Teclado físico
janela.bind("<Return>", lambda evento: calcular())
janela.bind("<Escape>", lambda evento: limpar())
janela.bind("<BackSpace>", lambda evento: apagar())

janela.mainloop()
