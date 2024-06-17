def soma_numeros(string_numeros):
    numeros = string_numeros.split(',')
    soma = sum(int(num) for num in numeros)
    return soma

string_numeros = "1,3,4,6,10,76"
print(soma_numeros(string_numeros))
