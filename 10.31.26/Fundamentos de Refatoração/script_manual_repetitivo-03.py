
import customtkinter as ctk
from tkinter import ttk, messagebox

# ======================================
# CONFIGURAÇÕES
# ======================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

produtos = [
    {"nome": "Mouse", "preco": 50.0, "quantidade": 10},
    {"nome": "Teclado", "preco": 150.0, "quantidade": 5},
    {"nome": "Monitor", "preco": 800.0, "quantidade": 2},
]

# ======================================
# FUNÇÕES
# ======================================

def alternar_tema():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")

def calcular_total(produto):
    return produto["preco"] * produto["quantidade"]


def atualizar_tabela(lista=None):
    tabela.delete(*tabela.get_children())

    dados = produtos if lista is None else lista

    for i, produto in enumerate(dados):
        tabela.insert(
            "",
            "end",
            iid=str(i),
            values=(
                produto["nome"],
                f"R$ {produto['preco']:.2f}",
                produto["quantidade"],
                f"R$ {calcular_total(produto):.2f}"
            )
        )

    atualizar_dashboard()


def atualizar_dashboard():
    total = len(produtos)
    unidades = sum(p["quantidade"] for p in produtos)
    valor = sum(calcular_total(p) for p in produtos)

    card_produtos.configure(text=str(total))
    card_unidades.configure(text=str(unidades))
    card_valor.configure(text=f"R$ {valor:,.2f}")


def cadastrar():
    nome = campo_nome.get().strip()

    try:
        preco = float(campo_preco.get().replace(",", "."))
        quantidade = int(campo_quantidade.get())

        if not nome or preco < 0 or quantidade < 0:
            raise ValueError

        produtos.append({
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        })

        limpar_campos()
        atualizar_tabela()

        messagebox.showinfo(
            "Sucesso",
            "Produto cadastrado com sucesso!"
        )

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Verifique os dados informados."
        )


def pesquisar():
    busca = campo_busca.get().strip().lower()

    encontrados = [
        p for p in produtos
        if busca in p["nome"].lower()
    ]

    tabela.delete(*tabela.get_children())

    for i, produto in enumerate(encontrados):
        tabela.insert(
            "",
            "end",
            iid=f"busca_{i}",
            values=(
                produto["nome"],
                f"R$ {produto['preco']:.2f}",
                produto["quantidade"],
                f"R$ {calcular_total(produto):.2f}"
            )
        )


def mostrar_todos():
    campo_busca.delete(0, "end")
    atualizar_tabela()


def excluir():
    selecionado = tabela.selection()

    if not selecionado:
        messagebox.showwarning(
            "Atenção",
            "Selecione um produto."
        )
        return

    nome = tabela.item(selecionado[0], "values")[0]

    produto = next(
        (p for p in produtos if p["nome"] == nome),
        None
    )

    if produto and messagebox.askyesno(
        "Confirmar",
        f"Deseja excluir {nome}?"
    ):
        produtos.remove(produto)
        atualizar_tabela()


def limpar_campos():
    campo_nome.delete(0, "end")
    campo_preco.delete(0, "end")
    campo_quantidade.delete(0, "end")


# ======================================
# JANELA PRINCIPAL
# ======================================

app = ctk.CTk()

app.title("Stock Manager")
app.geometry("1100x720")
app.minsize(900, 620)
app.configure(fg_color="#111827")


# ======================================
# MENU LATERAL
# ======================================
sidebar = ctk.CTkFrame(
    app,
    width=220,
    corner_radius=0,
    fg_color="#17243A"
)
sidebar.pack(side="left", fill="y")
sidebar.configure(fg_color="#0B1220")
sidebar.pack_propagate(False)


ctk.CTkLabel(
    sidebar,
    text="◆  STOCK MANAGER",
    font=("Segoe UI", 19, "bold"),
    text_color="#FFFFFF"
).pack(pady=(35, 45), padx=20)


ctk.CTkLabel(
    sidebar,
    text="MENU PRINCIPAL",
    font=("Segoe UI", 10, "bold"),
    text_color="#8D9BB0"
).pack(anchor="w", padx=25, pady=(0, 12))


ctk.CTkButton(
    sidebar,
    text="   ◈   Dashboard",
    anchor="w",
    height=42,
    fg_color="#29466D",
    hover_color="#345780",
    font=("Segoe UI", 13)
).pack(fill="x", padx=15, pady=4)


ctk.CTkButton(
    sidebar,
    text="   ▦   Produtos",
    anchor="w",
    height=42,
    fg_color="transparent",
    hover_color="#29466D",
    font=("Segoe UI", 13)
).pack(fill="x", padx=15, pady=4)


ctk.CTkLabel(
    sidebar,
    text="CONTROLE DE ESTOQUE",
    font=("Segoe UI", 10, "bold"),
    text_color="#8D9BB0"
).pack(anchor="w", padx=25, pady=(35, 12))


ctk.CTkLabel(
    sidebar,
    text="Sistema de gerenciamento\nVersão 1.0",
    font=("Segoe UI", 11),
    text_color="#AAB6C7",
    justify="left"
).pack(side="bottom", anchor="w", padx=22, pady=25)


# ======================================
# ÁREA PRINCIPAL
# ======================================

conteudo = ctk.CTkFrame(
    app,
    fg_color="transparent"
)
conteudo.pack(
    side="left",
    fill="both",
    expand=True,
    padx=30,
    pady=25
)


# Cabeçalho

ctk.CTkLabel(
    conteudo,
    text="Dashboard",
    font=("Segoe UI", 28, "bold"),
    text_color="#17243A"
).pack(anchor="w")


ctk.CTkLabel(
    conteudo,
    text="Visão geral do seu estoque",
    font=("Segoe UI", 13),
    text_color="#8993A4"
).pack(anchor="w", pady=(3, 22))


# ======================================
# CARDS DE INDICADORES
# ======================================

cards = ctk.CTkFrame(
    conteudo,
    fg_color="transparent"
)
cards.pack(fill="x", pady=(0, 25))


def criar_card(titulo, valor, coluna):
    card = ctk.CTkFrame(
        cards,
        fg_color="#1F2937",
        corner_radius=12,
        border_width=1,
        border_color="#374151"
    )

    card.grid(
        row=0,
        column=coluna,
        padx=(0, 12),
        sticky="nsew"
    )

    ctk.CTkLabel(
        card,
        text=titulo,
        font=("Segoe UI", 12),
        text_color="#8993A4"
    ).pack(anchor="w", padx=18, pady=(18, 5))

    label = ctk.CTkLabel(
        card,
        text=valor,
        font=("Segoe UI", 23, "bold"),
        text_color="#17243A"
    )

    label.pack(anchor="w", padx=18, pady=(0, 18))

    return label


cards.grid_columnconfigure((0, 1, 2), weight=1)

card_produtos = criar_card(
    "Produtos cadastrados", "0", 0
)

card_unidades = criar_card(
    "Unidades em estoque", "0", 1
)

card_valor = criar_card(
    "Valor do estoque", "R$ 0,00", 2
)


# ======================================
# CADASTRO
# ======================================

frame_cadastro = ctk.CTkFrame(
    conteudo,
    fg_color="#FFFFFF",
    corner_radius=12,
    border_width=1,
    border_color="#E8ECF2"
)

frame_cadastro.pack(fill="x", pady=(0, 20))


ctk.CTkLabel(
    frame_cadastro,
    text="Adicionar produto",
    font=("Segoe UI", 16, "bold"),
    text_color="#17243A"
).pack(anchor="w", padx=20, pady=(18, 12))


formulario = ctk.CTkFrame(
    frame_cadastro,
    fg_color="transparent"
)
formulario.pack(fill="x", padx=20, pady=(0, 18))


campo_nome = ctk.CTkEntry(
    formulario,
    placeholder_text="Nome do produto",
    height=40
)
campo_nome.pack(
    side="left",
    fill="x",
    expand=True,
    padx=(0, 10)
)


campo_preco = ctk.CTkEntry(
    formulario,
    placeholder_text="Preço",
    width=130,
    height=40
)
campo_preco.pack(side="left", padx=5)


campo_quantidade = ctk.CTkEntry(
    formulario,
    placeholder_text="Quantidade",
    width=130,
    height=40
)
campo_quantidade.pack(side="left", padx=5)


ctk.CTkButton(
    formulario,
    text="+ Adicionar",
    height=40,
    width=125,
    fg_color="#315EAB",
    hover_color="#254B8D",
    command=cadastrar
).pack(side="left", padx=(10, 0))


# ======================================
# TABELA E PESQUISA
# ======================================

frame_lista = ctk.CTkFrame(
    conteudo,
    fg_color="#FFFFFF",
    corner_radius=12,
    border_width=1,
    border_color="#E8ECF2"
)

frame_lista.pack(fill="both", expand=True)


topo_lista = ctk.CTkFrame(
    frame_lista,
    fg_color="transparent"
)
topo_lista.pack(fill="x", padx=20, pady=18)


ctk.CTkLabel(
    topo_lista,
    text="Produtos cadastrados",
    font=("Segoe UI", 16, "bold"),
    text_color="#17243A"
).pack(side="left")


campo_busca = ctk.CTkEntry(
    topo_lista,
    placeholder_text="Pesquisar produto...",
    width=200,
    height=35
)
campo_busca.pack(side="right", padx=5)


ctk.CTkButton(
    topo_lista,
    text="Buscar",
    width=75,
    height=35,
    command=pesquisar
).pack(side="right", padx=5)


# Estilo da tabela

estilo = ttk.Style()
estilo.theme_use("clam")

estilo.configure(
    "Treeview",
    background="#1F2937",
    foreground="#F9FAFB",
    fieldbackground="#1F2937",
    rowheight=42,
    font=("Segoe UI", 11),
    borderwidth=0
)

estilo.configure(
    "Treeview.Heading",
    background="#273449",
    foreground="#D1D5DB",
    font=("Segoe UI", 10, "bold"),
    relief="flat"
)

estilo.map(
    "Treeview",
    background=[("selected", "#315EAB")],
    foreground=[("selected", "#FFFFFF")]
)


frame_tabela = ctk.CTkFrame(
    frame_lista,
    fg_color="transparent"
)
frame_tabela.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=(0, 10)
)


colunas = (
    "Nome",
    "Preço",
    "Quantidade",
    "Total"
)

tabela = ttk.Treeview(
    frame_tabela,
    columns=colunas,
    show="headings"
)

for coluna in colunas:
    tabela.heading(coluna, text=coluna)
    tabela.column(coluna, anchor="center")

tabela.pack(fill="both", expand=True)


# ======================================
# RODAPÉ
# ======================================

rodape = ctk.CTkFrame(
    frame_lista,
    fg_color="transparent"
)
rodape.pack(fill="x", padx=20, pady=12)


ctk.CTkButton(
    rodape,
    text="Mostrar todos",
    width=110,
    fg_color="#E9EEF6",
    text_color="#34445C",
    hover_color="#D9E2EF",
    command=mostrar_todos
).pack(side="left")


ctk.CTkButton(
    rodape,
    text="Excluir selecionado",
    width=150,
    fg_color="#FCE8E8",
    text_color="#C33D45",
    hover_color="#F7D5D5",
    command=excluir
).pack(side="right")


# ======================================
# INICIALIZAÇÃO
# ======================================

atualizar_tabela()

app.mainloop()
