## Questões para Análise

- Quais filmes de comédia e animação tiveram nota media acima de 70 pontos?
- Quais são os atores mais frequentes dentre os filmes e series de comédia com nota média acima de 70?

## 1. Dockerfile

O `Dockerfile` é usado para criar uma imagem Docker que contém todas as dependências necessárias para executar o script Python que faz a ingestão de dados para o Amazon S3.

## 2. Script Python para Upload para S3

O script é responsável por fazer a ingestão de arquivos CSV para um bucket S3 na AWS. Ele realiza as seguintes tarefas:

- Importações: Importa bibliotecas necessárias (boto3, pandas, os, datetime e dotenv).
- Configurações: Carrega as variáveis de ambiente do arquivo .env e define configurações para o bucket S3 e os arquivos locais.
- Função upload_to_s3:
  Lê o arquivo CSV local.
  Define o caminho do arquivo no S3.
  Cria um cliente S3 usando as credenciais da AWS.
  Carrega o arquivo CSV para o bucket S3.
  Lida com possíveis exceções e imprime mensagens de erro ou sucesso.
- Execução Principal: Itera sobre os arquivos locais e chama a função upload_to_s3 para cada um.

## Comando para criar a imagem

 O comando ```docker build -t carregamento-s3 .``` cria uma imagem Docker chamada carregamento-s3 usando o Dockerfile localizado no diretório atual. Esta imagem pode então ser usada para criar contêineres que executam o script de upload para o S3.

## Comando para execultar o script no conteiner

O comando ```docker run --rm -v C:/Users/Vini/Documents/EstagioCompas/Sprint06/Desafio/Filmes+e+Series:/app/data carregamento-s3``` cria e executa um contêiner Docker a partir da imagem carregamento-s3, removendo o contêiner automaticamente após a execução (--rm). O diretório local C:/Users/Vini/Documents/EstagioCompass/Sprint06/Desafio/Filmes+e+Series é montado como /app/data dentro do contêiner (-v), permitindo que o script Python acesse e faça o upload dos arquivos CSV para o bucket S3 na AWS.

## Evidência do resultado no console AWS

![Evidencia 1](/Sprint6/evidencias/desafio1.png)
![Evidencia 2](/Sprint6/evidencias/desafio2.png)
![Evidencia 3](/Sprint6/evidencias/desafio3.png)