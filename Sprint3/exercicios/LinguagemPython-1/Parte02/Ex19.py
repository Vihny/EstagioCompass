import random

random_list = random.sample(range(500), 50)

random_list.sort()

valor_minimo = min(random_list)

valor_maximo = max(random_list)

media = sum(random_list) / len(random_list)

tamanho = len(random_list)
if tamanho % 2 == 0:
    mediana = (random_list[tamanho//2 - 1] + random_list[tamanho//2]) / 2
else:
    mediana = random_list[tamanho//2]

print(f"Media: {media:.2f}, Mediana: {mediana:.1f}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}")
