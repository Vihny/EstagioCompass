import sys
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql.functions import explode, row_number, col, split, trim, monotonically_increasing_id

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'INPUT_PATH_CSV', 'INPUT_PATH_JSON', 'OUTPUT_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

df_csv = spark.read.parquet(args['INPUT_PATH_CSV'])
df_json = spark.read.parquet(args['INPUT_PATH_JSON'])

df_csv = df_csv.withColumnRenamed("id", "id_imdb").withColumnRenamed("notaMedia", "notaMedia_csv")
df_json = df_json.withColumnRenamed("id", "id_imdb").withColumnRenamed("notaMedia", "notaMedia_json")

df_joined = df_csv.join(df_json, on="id_imdb", how="inner")

# Dimensão Tempo
window_spec_tempo = Window.orderBy(monotonically_increasing_id())

df_dim_tempo = df_joined.select(
    F.col("dataLancamento").alias("data_lancamento"),
    F.year("dataLancamento").alias("ano"),
    F.month("dataLancamento").alias("mes"),
    F.dayofmonth("dataLancamento").alias("dia")
).distinct()

df_dim_tempo = df_dim_tempo.withColumn("id_tempo", row_number().over(window_spec_tempo))

# Dimensão Gênero
df_with_genres = df_joined.withColumn("genero_array", split(col("genero"), ","))

df_exploded_genres = df_with_genres.withColumn("nome_genero", explode(col("genero_array")))

df_trimmed_genres = df_exploded_genres.withColumn("nome_genero", trim(col("nome_genero")))

df_dim_genero = df_trimmed_genres.select("nome_genero").distinct()

window_spec_genero = Window.orderBy("nome_genero")
df_dim_genero = df_dim_genero.withColumn("id_genero", row_number().over(window_spec_genero))

# Dimensão País
df_exploded_pais = df_joined.withColumn("nome_pais", explode(col("paisOrigem")))

df_dim_pais = df_exploded_pais.select("nome_pais").distinct()

window_spec_pais = Window.orderBy("nome_pais")
df_dim_pais = df_dim_pais.withColumn("id_pais", row_number().over(window_spec_pais))

# Dimensão Filme
df_dim_filme = df_joined.select(
    F.col("id_imdb").alias("id_filme"),
    F.col("tmdb_id").alias("id_tmdb"),
    F.col("tituloOriginal").alias("titulo_original")
).distinct()

# Tabela Fato Filme
df_fato = df_joined \
    .withColumn("id_filme", col("id_imdb")) \
    .withColumn("genero_array", split(col("genero"), ",")) \
    .withColumn("nome_genero", explode(col("genero_array"))) \
    .withColumn("nome_genero", trim(col("nome_genero"))) \
    .withColumn("nome_pais", explode(col("paisOrigem"))) \
    .withColumn("data_lancamento", col("dataLancamento")) \
    .withColumn("notaMedia_csv", col("notaMedia_csv").cast("double"))

df_fato = df_fato \
    .join(df_dim_genero, on="nome_genero", how="left") \
    .join(df_dim_pais, on="nome_pais", how="left") \
    .join(df_dim_tempo, on="data_lancamento", how="left") \
    .select(
        "id_filme",
        F.col("tituloPincipal").alias("titulo"),
        "receita",
        "notaMedia_csv",
        "id_genero",
        "id_pais",
        "id_tempo"
    ).distinct()

output_path = args['OUTPUT_PATH']

df_dim_tempo.write.mode('overwrite').parquet(f"{output_path}/Dim_Tempo/")
df_dim_genero.write.mode('overwrite').parquet(f"{output_path}/Dim_Genero/")
df_dim_pais.write.mode('overwrite').parquet(f"{output_path}/Dim_Pais/")
df_dim_filme.write.mode('overwrite').parquet(f"{output_path}/Dim_Filme/")
df_fato.write.mode('overwrite').parquet(f"{output_path}/Fato_Filme/")

spark.stop()