import boto3 # type: ignore

s3_client = boto3.client(
    's3',
    aws_access_key_id='ASIAVRUVSDBJVEVLRM5C',
    aws_secret_access_key='xK8e++SX3MMYsCIUZKTPbS6+RlqtcnCCeNubWG0M',
    aws_session_token='IQoJb3JpZ2luX2VjEKb//////////wEaCXVzLWVhc3QtMSJHMEUCIGQEyibgbghhS7Etnxda6G0XWtyJqyP4c8jVnusIXAlfAiEA9OD9Bsi7jFWuaKj7kOUIKatu2eFhrJP+F1nWP8BhWSQqowMIXxAAGgwzODE0OTIwMDkwNDMiDOOc+25quvLjBL3KxyqAAykqIEWu4rK/JZ+pLISvao5SE1NcjGjYqmN4KSZlaZ+z1LNW3PxrczLCr9WlUmcjWtYTSUg+5PJle5mzhYM//ydGTYErfqEqqRwAW3u12RA9f+LHhnsXwJpG9rJ70DBsb5eqZygWCkqNJ9OoP0woERXxynu2d2oAfJ1eGQ4ZBN7Xbh15VfYWAosT6Xtu5LhcQ4ft7lYH9GOHeI2g/m98spBIskkILfME+Dh3i7AUE+GkI66tqgrSfxIxLw73Kp3rLD9wIy/A/SG2g8fLDckXpK6B4+SEp1Q6E8XeL3Ig4cmmbsZfBNX0tfeWEJHhSsSlpn/BCfGwr5qVoRzsGtDLk+cENwNR4/IqL2xSZe3FUCY8+noUYVmXRKMr5/RrCJ/vWyabTykTBK+ExwRTvd0Y6UD1PvtWrwDuu2+wkXOPFvuie0GDAxCrXgow/zn2eFyE7+8YcGBXPu+f2hGemjBbCJYLErwJTy3tknXT4xjBGMEgQ4iKJEsjISFSRW+7v6sF8zDK34q0BjqmAXEaYTFbrkhEgfzbpbUCjMhkqu86F5pSWIKjn3ZHaUUbuyYQZ6zAfx1FfwMHjHOmpdgOEqt8mfNOxwWdsbbTmJrD4Q5xWHHTu+ST3a32nOoM44X54HYUC9gQIO3szohnOZMauR28OmUgs5Pxk2V15x2Aq8CslaUCnXf0TVDCT7Y5cOsRnr0T9qDK0tMVXbPpdekbkb4Z+kzNvEp6cQl6YV368JJpPWQ='
)

bucket_name = 'my-bucket-de-dados'
file_name = 'Preços semestrais - AUTOMOTIVOS_2023.02.csv'

query ="""
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

response = s3_client.select_object_content(
    Bucket=bucket_name,
    Key=file_name,
    ExpressionType='SQL',
    Expression=query,
    InputSerialization={
        'CSV': {
            'FileHeaderInfo': 'USE',
            'RecordDelimiter': '\n',
            'FieldDelimiter': ';'
        }
    },
    OutputSerialization={
        'CSV': {}
    }
)

for event in response['Payload']:
    if 'Records' in event:
        records = event['Records']['Payload'].decode('utf-8')
        print(records)
