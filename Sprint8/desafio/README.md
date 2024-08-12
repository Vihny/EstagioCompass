## Questões para Análise e API Utilizada

 Para a injestão de novos dados foi utilizado a API do TMDB, que é uma excelente escolha devido à sua riqueza de informações e atualizações frequentes. Além disso, a API é fácil de integrar com bibliotecas populares de programação, facilitando a coleta e análise de dados de forma eficiente.

- Quais filmes de animação tiveram nota média maior ou igual 8.0 pontos entre 2010 a 2020?
  - Denter esses filmes, quais tiveram receita acima de R$100 milhões?
  - Denter esses filmes, quais  foram produzidos no Japão?

## 1. Script Python JobCSV

JobCSV. [script](/Sprint8/desafio/JobCSV.py)

Spark: Utiliza Spark para ler um arquivo CSV.
Transformações e Filtragem: Divide a coluna de gêneros, filtra por animação, nota alta e ano de lançamento.
Limpeza: Remove colunas desnecessárias e elimina duplicados.
Salvamento: Salva os dados processados em formato Parquet no S3.

## 2. Script Python JobJSOM

JobJSOM. [script](/Sprint8/desafio/JobJSOM.py)

Spark e GlueContext: Utiliza Spark e GlueContext para ler dados JSON do S3.
Transformações: Renomeia colunas e preenche valores nulos.
Particionamento: Extrai e formata data do caminho do arquivo para particionamento.
Salvamento: Escreve dados em formato Parquet no S3 com particionamento.

## 3. Evidências da execução no AWS Glue e resultado no Bucket S3.

![Evidencia 1](/Sprint8/evidencias/EvidenciaGlue1.png)
![Evidencia 2](/Sprint8/evidencias/EvidenciaGlue2.png)
![Evidencia 3](/Sprint8/evidencias/EvidenciaGlue3.png)
![Evidencia 4](/Sprint8/evidencias/EvidenciaGlue4.png)