import random
import names

# Definir semente de aleatoriedade
random.seed(40)

# Quantidade de nomes únicos e aleatórios
qtd_nomes_unicos = 3608
qtd_nomes_aleatorios = 10000000

# Lista para armazenar nomes
aux = []
dados = []

# Gerar nomes únicos
for _ in range(qtd_nomes_unicos):
    aux.append(names.get_full_name())

print(f"Gerando {qtd_nomes_aleatorios} nomes aleatórios")

# Gerar nomes aleatórios com base nos nomes únicos
for _ in range(qtd_nomes_aleatorios):
    dados.append(random.choice(aux))

with open('names_aleatorios.txt', 'w') as f:
    for nome in dados:
        f.write(f"{nome}\n")
