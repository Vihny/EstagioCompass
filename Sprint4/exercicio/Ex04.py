def calcular_valor_maximo(operadores, operandos) -> float:
    operacoes = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else float('inf'),
        '%': lambda x, y: x % y if y != 0 else float('inf'),
    }

    resultados = map(lambda operacao: operacoes[operacao[0]](*operacao[1]), zip(operadores, operandos))

    valor_maximo = max(resultados)

    return valor_maximo
