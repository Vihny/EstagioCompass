dados = []
with open('actors.csv', 'r') as arquivo:
    linhas = arquivo.readlines()
    cabecalho = linhas[0].strip().split(',')
    for linha in linhas[1:]:
        valores = linha.strip().split(',')
        dados.append(dict(zip(cabecalho, valores)))

ator_com_mais_filmes = max(dados, key=lambda x: float(x['Number of Movies']))
with open('etapa-1.txt', 'w') as arquivo:
    arquivo.write("Ator com mais filmes: " + f"{ator_com_mais_filmes['Actor']} {ator_com_mais_filmes['Number of Movies']}")

media_receita = sum(float(x['Gross']) for x in dados) / len(dados)
with open('etapa-2.txt', 'w') as arquivo:
    arquivo.write("Media da receita: " + str(media_receita))

ator_com_maior_media = max(dados, key=lambda x: float(x['Average per Movie']))
with open('etapa-3.txt', 'w') as arquivo:
    arquivo.write("Ator com maior média de receita bilhetaria bruta por filme: "+f"{ator_com_maior_media['Actor']} {ator_com_maior_media['Average per Movie']}")

contagem_filmes = {}
for ator in dados:
    if ator['#1 Movie'] not in contagem_filmes:
        contagem_filmes[ator['#1 Movie']] = 0
    contagem_filmes[ator['#1 Movie']] += 1
filmes_ordenados = sorted(contagem_filmes.items(), key=lambda x: (-x[1], x[0]))
with open('etapa-4.txt', 'w') as arquivo:
    for filme, contagem in filmes_ordenados:
        arquivo.write(f"O filme {filme} aparece {contagem} vez(es) no dataset\n")

atores_ordenados = sorted(dados, key=lambda x: -float(x['Total Gross']))
with open('etapa-5.txt', 'w') as arquivo:
    for ator in atores_ordenados:
        arquivo.write(f"{ator['Actor']} {ator['Total Gross']}\n")
        

