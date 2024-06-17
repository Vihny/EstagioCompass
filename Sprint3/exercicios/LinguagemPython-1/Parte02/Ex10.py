lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

def remove_duplicados(lista):
    return list(set(lista))


print(remove_duplicados(lista))
