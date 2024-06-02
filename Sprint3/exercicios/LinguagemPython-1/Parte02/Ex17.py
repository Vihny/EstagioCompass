def divide_lista(lista):
    tamanho = len(lista)
    tamanho_parte = tamanho // 3
    return [lista[i:i+tamanho_parte] for i in range(0, tamanho, tamanho_parte)]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
listas_divididas = divide_lista(lista)

lista1, lista2, lista3 = listas_divididas

print(lista1, lista2, lista3)


