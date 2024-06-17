import csv

def processar_notas(arquivo):
    with open(arquivo, 'r') as f:
        reader = csv.reader(f)
        estudantes = list(reader)

    relatorio = []
    for estudante in estudantes:
        nome = estudante[0]
        notas = list(map(int, estudante[1:]))
        tres_maiores_notas = sorted(notas, reverse=True)[:3]
        media = round(sum(tres_maiores_notas) / 3, 2)
        relatorio.append((nome, tres_maiores_notas, media))

    relatorio.sort()

    for nome, notas, media in relatorio:
        print(f"Nome: {nome} Notas: {notas} Média: {media}")

processar_notas('estudantes.csv')