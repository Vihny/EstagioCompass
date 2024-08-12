from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, when, rand, expr
from pyspark import SparkConf
from pyspark.sql.types import StringType, IntegerType
import random

spark = SparkSession.builder.master("local[*]").appName("Exercicio").getOrCreate()
spark_conf = SparkConf().setAppName("Exercicio").set("spark.eventLog.enabled", "false")
spark = SparkSession.builder.config(conf=spark_conf).getOrCreate()
spark.sparkContext.setLogLevel("WARN")

df_nomes = spark.read.csv("/home/vini/ExSpark/names_aleatorios.txt", header=False, inferSchema=True)
df_nomes.show(5)

df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")
df_nomes.printSchema()
df_nomes.show(10)

df_nomes = df_nomes.withColumn(
    'Escolaridade',
    when(rand() < 1/3, 'Fundamental')
    .when(rand() < 2/3, 'Medio')
    .otherwise('Superior')
)

paises = ["Argentina", "Bolivia", "Brasil", "Chile", "Colombia", "Ecuador", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguai", "Venezuela"]

df_nomes = df_nomes.withColumn(
    'Pais',
    expr(f"CASE WHEN rand() < 1/12 THEN '{paises[0]}' "
         f"WHEN rand() < 2/12 THEN '{paises[1]}' "
         f"WHEN rand() < 3/12 THEN '{paises[2]}' "
         f"WHEN rand() < 4/12 THEN '{paises[3]}' "
         f"WHEN rand() < 5/12 THEN '{paises[4]}' "
         f"WHEN rand() < 6/12 THEN '{paises[5]}' "
         f"WHEN rand() < 7/12 THEN '{paises[6]}' "
         f"WHEN rand() < 8/12 THEN '{paises[7]}' "
         f"WHEN rand() < 9/12 THEN '{paises[8]}' "
         f"WHEN rand() < 10/12 THEN '{paises[9]}' "
         f"WHEN rand() < 11/12 THEN '{paises[10]}' "
         f"ELSE '{paises[11]}' END")
)

df_nomes = df_nomes.withColumn(
    'AnoNascimento',
    (rand() * (2010 - 1945) + 1945).cast(IntegerType())
)
df_nomes.printSchema()

df_select = df_nomes.filter(col("AnoNascimento") >= 2000)
df_select.show(10)

df_nomes.createOrReplaceTempView("pessoas")
spark.sql("SELECT * FROM pessoas WHERE AnoNascimento >= 2000").show(10)

num_millennials = df_nomes.filter((col("AnoNascimento") >= 1980) & (col("AnoNascimento") <= 1994)).count()
print(f"--------------------------------------------------")
print(f"Número de Millennials: {num_millennials}")
print(f"--------------------------------------------------")

num_millennials_sql = spark.sql("SELECT COUNT(*) FROM pessoas WHERE AnoNascimento BETWEEN 1980 AND 1994").collect()[0][0]
print(f"--------------------------------------------------")
print(f"Número de Millennials (SQL): {num_millennials_sql}")
print(f"--------------------------------------------------")

result = spark.sql("""
    SELECT
        Pais,
        CASE
            WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
            WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
            WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
            WHEN AnoNascimento BETWEEN 1995 AND 2015 THEN 'Geração Z'
        END AS Geracao,
        COUNT(*) AS Quantidade
    FROM pessoas
    GROUP BY Pais, Geracao
    ORDER BY Pais, Geracao
""")
result.show()
