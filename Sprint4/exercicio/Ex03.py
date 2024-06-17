from functools import reduce

def calcula_saldo(lancamentos):
    valores = map(lambda lancamento: lancamento[0] if lancamento[1] == 'C' else -lancamento[0], lancamentos)

    saldo = reduce(lambda a, b: a + b, valores)

    return saldo
