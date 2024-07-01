SELECT
    UPPER (s."Regiao - Sigla"),
    UPPER (s."Estado - Sigla"),
    s."Municipio",
    s."Revenda",
    s."CNPJ da Revenda",
    CAST(s."Nome da Rua" AS STRING) AS numero_rua_string,
    CAST(s."Numero Rua" AS STRING) AS numero_rua_string,
    CAST(s."Complemento" AS STRING) AS numero_rua_string,
    CAST(s."Bairro" AS STRING) AS numero_rua_string,
    s."Cep",
    s."Produto",
    s."Data da Coleta",
    s."Valor de Venda",
    s."Valor de Compra",
    s."Unidade de Medida",
    s."Bandeira",
    CASE
        WHEN s."Valor de Venda" > '5' THEN 'Alto'
        ELSE 'Baixo'
    END as classificacao_valor
FROM s3object s
WHERE (s."Municipio" = 'CAMPINA GRANDE' OR s."Municipio" = 'SANTO ANGELO')
    AND (s."Produto" = 'GASOLINA' OR s."Produto" = 'ETANOL')
"""