with open('number.txt', 'r') as f:
    numeros = list(map(int, f.read().splitlines()))

pares = list(filter(lambda x: x % 2 == 0, numeros))
pares_ordenados = sorted(pares, reverse=True)
cinco_maiores_pares = pares_ordenados[:5]
soma = sum(cinco_maiores_pares)

print(cinco_maiores_pares)
print(soma)
