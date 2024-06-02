def my_map(lista, listaPotencia):
    return [listaPotencia(x) for x in lista]

def quadrado(x):
    return x ** 2

print(my_map([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], quadrado))
