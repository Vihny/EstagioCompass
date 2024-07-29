## Questões para Análise e API Utilizada

 Para a injestão de novos dados foi utilizado a API do TMDB, quue é uma excelente escolha devido à sua riqueza de informações e atualizações frequentes. Além disso, a API é fácil de integrar com bibliotecas populares de programação, facilitando a coleta e análise de dados de forma eficiente.

- Quais filmes de animação tiveram nota média acima de 8.0 pontos entre 2010 a 2020?
  - Denter esses filmes, uais tiveram receita acima de $100 milhões?
  - Denter esses filmes, quais  foram produzidos no Japão?

## 1. Docker

 - O `Dockerfile` é usado para criar uma imagem Docker que contém todas as dependências necessárias para executar o script Python que faz a ingestão de dados da API para o Amazon S3. O comando ```docker build -t api-layer .``` cria uma imagem Docker chamada api-layer usando o Dockerfile localizado no diretório atual.


- O comando ```docker run --rm -v C:\Users\Vini\Documents\EstagioCompas\Sprint07\desafio\desafio2:/app api-layer``` cria e executa um contêiner Docker a partir da imagem api-layer, removendo o contêiner automaticamente após a execução (--rm). O diretório local C:/Users/Vini/Documents/EstagioCompass/Sprint06/desafio/desafio2 é montado como /app dentro do contêiner (-v), permitindo que o script Python acesse e faça o upload dos dados no bucket.

## 3. Script Python para Upload S3: máquina local

Diretório. [DesafioMaquinaLocal](/Sprint7/desafio/desafioMaquilaLocal/)

O script é responsável por coletar dados de filmes de animação da API do TMDB e armazenar esses dados em um bucket S3 na AWS. Ele realiza as seguintes tarefas:

- Importações: Importa as bibliotecas necessárias (os, json, requests, boto3, datetime).
- Configurações: Configura o cliente S3 usando boto3.
 Define o nome do bucket e a chave da API do TMDB a partir das variáveis de ambiente. Define o ID do gênero de animação (16).
- Função fetch_movies_by_genre: Coleta dados de filmes de animação da API do TMDB. Faz a paginação dos resultados até um máximo de 500 páginas. Filtra filmes com nota média maior ou igual a 8 e lançados entre 2010 e 2020. Para cada filme, obtém detalhes adicionais, como título, países de origem e receita.
- Função fetch_movie_details: Coleta detalhes de um filme específico da API do TMDB.
- Função save_to_s3: Salva os dados coletados no bucket S3 em arquivos JSON. Divide os dados em chunks de 100 registros para garantir que cada arquivo tenha no máximo 100 registros. Define o caminho do arquivo no S3 e carrega os dados.
- Função lambda_handler: Função principal que é executada como uma função Lambda. Coleta dados de filmes de animação e salva no S3. Lida com possíveis exceções e retorna mensagens de erro ou sucesso.

## 4. Script Python para Upload S3: Lambda

Arquivo PY Lambda. [Lambda.py](/Sprint7/desafio/Lambda2.0.py)

O script é responsável por coletar dados de filmes de animação da API do TMDB e armazenar esses dados em um bucket S3 na AWS. Ele realiza as seguintes tarefas:

- Importações: Importa as bibliotecas necessárias (json, requests, boto3, datetime).
-Configurações: Configura o cliente S3 usando boto3.Define o nome do bucket e a chave da API do TMDB a partir das variáveis de ambiente. Define o ID do gênero de animação (16).
- Função fetch_movies_by_genre: Coleta dados de filmes de animação da API do TMDB. Faz a paginação dos resultados até um máximo de 500 páginas. Filtra filmes com nota média maior ou igual a 8 e lançados entre 2010 e 2020. Para cada filme, obtém detalhes adicionais, como título, países de origem e receita.
- Função fetch_movie_details: Coleta detalhes de um filme específico da API do TMDB.
- Função save_to_s3: Salva os dados coletados no bucket S3 em arquivos JSON. Divide os dados em chunks de 100 registros para garantir que cada arquivo tenha no máximo 100 registros. Define o caminho do arquivo no S3 e carrega os dados.
- Função lambda_handler: Função principal que é executada como uma função Lambda. Coleta dados de filmes de animação e salva no S3. Lida com possíveis exceções e retorna mensagens de erro ou sucesso.

## 5. Evidências do resultado no Bucket S3 e o Teste do Lanbda

![Evidencia 1](/Sprint7/evidencias/desafiolam.png)
![Evidencia 2](/Sprint7/evidencias/desafios3.png)