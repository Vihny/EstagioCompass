## Questões para Análise e API Utilizada

 Para a injestão de dados foi utilizado a API do TMDB, que é uma excelente escolha devido à sua riqueza de informações e atualizações frequentes. Além disso, a API é fácil de integrar com bibliotecas populares de programação, facilitando a coleta e análise de dados de forma eficiente.

- Filmes do gênero animação que tiveram nota média maior ou igual 8.0 pontos, entre 2010 a 2020.
  - Denter esses filmes, quais tiveram receita acima de R$100 milhões?
  - Denter esses filmes, quais  foram produzidos no Japão?

## 1. Script Python JobCamadaRefined

JobCamadaRefined - [script](/Sprint9/desafio/JobCamadaRefined.py)

- Importações: Importa as bibliotecas necessárias para o job, incluindo sys, pyspark, e awsglue.
- Configurações: Configura o contexto do Glue e Spark, e lê os parâmetros do job (como caminhos de entrada e saída) usando getResolvedOptions.
- Carregamento dos Dados: Lê os arquivos Parquet da camada Trusted para os DataFrames df_csv e df_json, renomeando colunas para facilitar a junção.
- Junção dos Dados: Realiza a junção entre os DataFrames df_csv e df_json com base no campo id_imdb, consolidando as informações dos filmes.
- Criação das Dimensões
  - Dimensão Tempo: Cria a tabela de dimensão Dim_Tempo, que contém informações de data, ano, mês e dia, associadas a cada filme.
  - Dimensão Gênero: Processa os dados de gênero, criando a dimensão Dim_Genero, que associa cada gênero de filme a um identificador único.
  - Dimensão País: Processa os dados de países de origem dos filmes, criando a dimensão Dim_Pais, com identificadores únicos para cada país.
  - Dimensão Filme: Cria a dimensão Dim_Filme, que contém os IDs dos filmes, IDs do TMDB e os títulos originais dos filmes.
- Criação da Tabela de Fatos: Monta a tabela Fato_Filme, que combina os IDs das dimensões com as métricas dos filmes, como receita e nota média, e os salva.
- Salvamento das Tabelas: Salva as dimensões (Dim_Tempo, Dim_Genero, Dim_Pais, Dim_Filme) e a tabela de fatos (Fato_Filme) no S3 em formato Parquet, dentro do caminho especificado.


## 3. Evidências do Desafio

- Modelagem dimensional
![Evidencia 1](/Sprint9/evidencias/Modelagemdimensional.png)

- AWS console
![Evidencia 2](/Sprint9/evidencias/DesafioJobGlue.png)
![Evidencia 3](/Sprint9/evidencias/DesafioJobGlue2.png)
![Evidencia 4](/Sprint9/evidencias/DesafioCrawler.png)
![Evidencia 5](/Sprint9/evidencias/DesafioCrawler2.png)