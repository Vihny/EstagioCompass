import sys
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql.functions import lit, col
from pyspark.sql.types import DateType
import re

# @params: [JOB_NAME, INPUT_PATH, OUTPUT_PATH]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'INPUT_PATH', 'OUTPUT_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

input_path = args['INPUT_PATH']
output_path = args['OUTPUT_PATH']

df = glueContext.create_dynamic_frame_from_options(
    connection_type="s3",
    connection_options={"paths": [input_path]},
    format="json"
).toDF()

df = df.withColumnRenamed("imdb_id", "id") \
       .withColumnRenamed("title", "titulo") \
       .withColumnRenamed("countries_of_origin", "paisOrigem") \
       .withColumnRenamed("revenue", "receita") \
       .withColumnRenamed("release_year", "dataLancamento") \
       .withColumnRenamed("vote_average", "notaMedia")

df = df.fillna({
    'id': 0 ,         
    'receita': 0,                 
    'notaMedia': 0.0              
})

match = re.search(r"/(\d{4})/(\d{2})/(\d{2})/", input_path)
if match:
    year, month, day = match.groups()
    partition_date = f"{year}\{month}\{day}"
    formatted_partition = f"dt={partition_date}"
else:
    raise ValueError("O caminho de entrada não contém uma data válida no formato yyyy/MM/dd.")

df = df.withColumn("dt", lit(partition_date))

output_dir = f"{output_path}/dt={partition_date}/"

df.coalesce(1).write.mode("overwrite").parquet(output_dir)

spark.stop()