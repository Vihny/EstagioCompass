import sys
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql.functions import col, array_contains, split, lit

# @params: [JOB_NAME, INPUT_PATH, OUTPUT_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'INPUT_PATH', 'OUTPUT_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

print("Iniciando a leitura do CSV...")
df = spark.read.option("header", "true").option("delimiter", ",").csv(args['INPUT_PATH'])

print("Dividindo a coluna 'genero'...")
df_with_genres = df.withColumn("generos_array", split(col("genero"), ","))

df_filtered = df_with_genres.filter(
    array_contains(col("generos_array"), "Animation") & 
    (col("notaMedia").cast("float") >= 8) &
    (col("anoLancamento").cast("int").between(2010, 2020))
)

columns_to_drop = [
    "tempoMinutos", "numeroVotos", "generoArtista", "personagem", 
    "nomeArtista", "anoNascimento", "anoFalecimento", "profissao", 
    "titulosMaisConhecidos", "generos_array",  
]
df_cleaned = df_filtered.drop(*columns_to_drop)

df_unique = df_cleaned.dropDuplicates(["id"])

print("Salvando os dados no formato Parquet...")
df_unique.write.mode('overwrite').parquet(args['OUTPUT_PATH'])

print("Encerrando a sessão do Spark...")
spark.stop()