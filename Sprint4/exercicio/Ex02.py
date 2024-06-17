def conta_vogais(texto: str) -> int:
    vogais = 'aeiouAEIOU'

    vogais_no_texto = filter(lambda letra: letra in vogais, texto)
    numero_de_vogais = len(list(vogais_no_texto))

    return numero_de_vogais
