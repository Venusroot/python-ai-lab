# Uma vez instalada, a biblioteca Pandas DEVE SER "CHAMADA" assim...
import pandas as pd #pd é uma apelido.

# Criar uma base de dados local para acesso com o Pandas
dados = {
    "Nome": ["Ana", "Bruno", "Carlos", "Patricia"],
    "Notas": [10, 4, 0, 9],
    "Comentários": ["Excelente aluna", "Esforçado", "Precisa de mais dedicação", "Melhorando"]
}
# O Pandas usa um DataFrame para acessar uma base de dados.
# Obrigatório o uso de DataFrames no Pandas
df = pd.DataFrame(dados)

# Exibir os Dados do DataFrame df
print(df.head())
