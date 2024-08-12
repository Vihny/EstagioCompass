# Lista de 20 nomes de animais
animais = [
    'cachorro', 'gato', 'elefante', 'leão', 'tigre', 'urso', 'rato', 'coelho', 
    'pássaro', 'peixe', 'cavalo', 'cobra', 'jacaré', 'tartaruga', 'giraffe', 
    'pinguim', 'macaco', 'golfinho', 'porco', 'ovelha', 'vaca'
]

# Ordenar a lista
animais.sort()

# Iterar e imprimir os nomes
for animal in animais:
    print(animal)

# Armazenar a lista em um arquivo CSV
with open('animais.csv', 'w') as f:
    for animal in animais:
        f.write(f"{animal}\n")
