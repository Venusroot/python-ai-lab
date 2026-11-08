
def somar_idades(idade1, idade2):
    """Recebe duas idades e retorna a soma."""
    return idade1 + idade2


# Primeiro grupo de idades
idade1 = 20
idade2 = 25

soma1 = somar_idades(idade1, idade2)

print("=== Primeiro Grupo ===")
print(f"Idade 1: {idade1}")
print(f"Idade 2: {idade2}")
print(f"Soma das idades: {soma1}")


# Segundo grupo de idades
idade3 = 30
idade4 = 35

soma2 = somar_idades(idade3, idade4)

print("\n=== Segundo Grupo ===")
print(f"Idade 3: {idade3}")
print(f"Idade 4: {idade4}")
print(f"Soma das idades: {soma2}")


# Soma total de todas as idades
soma_total = soma1 + soma2

print("\n=== Resultado Final ===")
print(f"Soma total das idades: {soma_total}")
