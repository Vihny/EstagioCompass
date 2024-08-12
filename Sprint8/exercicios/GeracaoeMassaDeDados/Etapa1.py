import random

# Inicializar a lista com 250 inteiros aleatórios
lista = [random.randint(1, 1000) for _ in range(250)]

# Reverter a lista
lista.reverse()

# Imprimir o resultado
print(lista)
