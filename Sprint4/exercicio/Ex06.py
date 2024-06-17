def maiores_que_media(conteudo: dict) -> list:
    media = sum(conteudo.values()) / len(conteudo)

    produtos_acima_da_media = filter(lambda item: item[1] > media, conteudo.items())

    produtos_ordenados = sorted(produtos_acima_da_media, key=lambda item: item[1])

    return produtos_ordenados
