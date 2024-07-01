## Dados Utilizados

 - Em cumprimento às determinações da Lei do Petróleo (Lei nº 9478/1997, artigo 8º), a ANP acompanha os preços praticados por revendedores de combustíveis automotivos, por meio de uma pesquisa semanal de preços realizada por empresa contratada. Nesse desafio foi utilizado os dados referente ao 2° semestre do ano de 2022, que possui as seguintes informações Regiao, Estado, Municipio, Revenda, CNPJ da Revenda, Nome da Rua, Numero Rua, Complemento, Bairro, Cep, Produto, Data da Coleta, Valor de Venda,Valor de Compra, Unidade de Medida e Bandeira.

## Consulta Realizada - Resultado

 A consulta realizada foi pra selecionar os dados de todas as colunas onde os municípios seja Campina Grande e Santo Angelo, no qual os produtos revendidos for gasolina ou etanol, adicionando uma classificação ao preço de cada revenda, sendo "Alto" caso o valor seja maior que 5 e "Baixo" caso seja menor. Os dados de algumas colunas foram convertidos para deixar no tipo desejado.

 - No SELECT foi definido as colunas que retornaram a consulta. O UPPER foi utilizado para converter o valor da coluna "Estado - Sigla" e "Regiao - Sigla" para maiúsculas, essa função transforma todas as letras minúsculas em maiúsculas. O CAST foi utilizado converter o valor da coluna de endereço("Nome da Rua", "Numero Rua", "Complemento", "Bairro" )para o tipo STRING e o renomeia o nome das colunas de acordo a alteração, essa função é usada para converter tipos de dados. O CASE foi utilizado para criar uma nova coluna chamada classificacao_valor baseada na condição fornecida, essa função é usada para realizar verificações condicionais e retornar um valor específico baseado nessas condições. As demais colunas tiveram o retorno sem alteração.

 - O FROM define a origem dos dados, a consulta está sendo feita a partir de um objeto S3 chamado s3object e que o alias para esse objeto é s. 

 - O WHERE Define as condições que os registros devem satisfazer para serem incluídos no resultado. Filtrando os registros com OR para incluir apenas o valor 'CAMPINA GRANDE' ou 'SANTO ANGELO' da coluna "Municipio", mais uma condição adicional para incluir apenas os registros onde o valor da coluna "Produto" é 'GASOLINA' ou 'ETANOL'. Ambas as condições são combinadas com um AND, significando que ambas devem ser satisfeitas para que o registro seja incluído no resultado.

 ![Primeiro dados da tabela](/Sprint5/evidencias/evidencia1.png)
 ![Dados do município Santo Angelo](/Sprint5/evidencias/evidencia2.png)