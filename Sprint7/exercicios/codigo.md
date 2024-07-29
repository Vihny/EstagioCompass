### Código utilizado para contar as palavras do README no Spark Shell

```
val filePath = "/tmp/README.md"
   val df = spark.read.text(filePath)

import org.apache.spark.sql.functions._
val words = df.select(explode(split(col("value"), "\\s+")).alias("word"))
val wordCounts = words.groupBy("word").count()

wordCounts.show(truncate = false, numRows = 1000)
```

### Código utilizado no Job do Glue

```
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F

# @params: [JOB_NAME, S3_INPUT_PATH, S3_TARGET_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args['S3_INPUT_PATH']
df = spark.read.csv(source_file, header=True, inferSchema=True)

df.printSchema()

df = df.withColumn("nome", F.upper(F.col("nome")))

num_linhas = df.count()
print(f"Contagem de linhas: {num_linhas}")

contagem_nomes = df.groupBy("ano", "sexo").count()
contagem_nomes.show()

df = df.orderBy(F.desc("ano"))

nome_feminino = df.filter(F.col("sexo") == "F")
nome_feminino_max = nome_feminino.groupBy("nome", "ano").agg(F.sum("total").alias("total")).orderBy(F.desc("total")).first()
print(f"Nome feminino com mais registros: {nome_feminino_max['nome']} no ano {nome_feminino_max['ano']}")

nome_masculino = df.filter(F.col("sexo") == "M")
nome_masculino_max = nome_masculino.groupBy("nome", "ano").agg(F.sum("total").alias("total")).orderBy(F.desc("total")).first()
print(f"Nome masculino com mais registros: {nome_masculino_max['nome']} no ano {nome_masculino_max['ano']}")

total_registros = df.groupBy("ano").agg(F.sum("total").alias("total"))
total_registros.show()

primeiras_10_linhas = df.orderBy("ano").limit(10)
primeiras_10_linhas.show()

target_path = args['S3_TARGET_PATH']
df.write \
    .mode("overwrite") \
    .partitionBy("sexo", "ano") \
    .json(f"{target_path}/frequencia_registro_nomes_eua/")

job.commit()
```