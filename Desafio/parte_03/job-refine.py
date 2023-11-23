import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH_1', 'S3_INPUT_PATH_2', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file_1 = args['S3_INPUT_PATH_1']
source_file_2 = args['S3_INPUT_PATH_2']
target_path = args['S3_TARGET_PATH']

df1 = spark.read.parquet(source_file_1)
df2 = spark.read.parquet(source_file_2)

# Faz a junção usando as colunas de referência
join_condition = df1["id_imdb"] == df2["imdb_id"]
joined_df = df1.join(df2, join_condition, "inner")

# Desaninhar a coluna pertence_coletanea"
collection_columns = ["id", "name", "poster_path", "backdrop_path"]
for col_name in collection_columns:
    joined_df = joined_df.withColumn(col_name, joined_df["pertence_coletanea"].getItem(col_name))

# Remover a coluna aninhada
joined_df = joined_df.drop("pertence_coletanea")

# Renomear colunas desaninhadas, se necessário
renamed_columns = {
    "id": "id_coletanea",
    "name": "nome_coletanea",
    "poster_path": "poster_coletanea",
    "backdrop_path": "cartaz_coletanea"
}
for old_name, new_name in renamed_columns.items():
    joined_df = joined_df.withColumnRenamed(old_name, new_name)
 
 
    

# Desaninhar a coluna "genero_filme"
genero_columns = ["id", "name"]
for col_name in genero_columns:
    joined_df = joined_df.withColumn(col_name, joined_df["genero_filme"].getItem(col_name))

# Remover a coluna aninhada
joined_df = joined_df.drop("genero_filme")

# Renomear colunas desaninhadas, se necessário
renamed_columns = {
    "id": "id_genero_filme",
    "name": "nome_genero_filme"
}
for old_name, new_name in renamed_columns.items():
    joined_df = joined_df.withColumnRenamed(old_name, new_name)
 
 
    
    
# Desaninhar a coluna produtora_filme"
collection_columns = ["id", "name", "logo_path", "origin_country"]
for col_name in collection_columns:
    joined_df = joined_df.withColumn(col_name, joined_df["produtora_filme"].getItem(col_name))

# Remover a coluna aninhada
joined_df = joined_df.drop("produtora_filme")

# Renomear colunas desaninhadas, se necessário
renamed_columns = {
    "id": "id_produtora_filme",
    "name": "nome_produtora_filme",
    "logo_path": "logo_produtora_filme",
    "origin_country": "pais_origem_produtora"
}
for old_name, new_name in renamed_columns.items():
    joined_df = joined_df.withColumnRenamed(old_name, new_name)    
  
  
    
    
# Desaninhar a coluna "pais_producao"
genero_columns = ["iso_3166_1", "name"]
for col_name in genero_columns:
    joined_df = joined_df.withColumn(col_name, joined_df["pais_producao"].getItem(col_name))

# Remover a coluna aninhada
joined_df = joined_df.drop("pais_producao")

# Renomear colunas desaninhadas, se necessário
renamed_columns = {
    "iso_3166_1": "sigla_pais_producao",
    "name": "nome_pais_producao"
}
for old_name, new_name in renamed_columns.items():
    joined_df = joined_df.withColumnRenamed(old_name, new_name)



# Desaninhar a coluna "idioma_falado_filme"
genero_columns = ["english_name", "iso_639_1", "name"]
for col_name in genero_columns:
    joined_df = joined_df.withColumn(col_name, joined_df["idioma_falado_filme"].getItem(col_name))

# Remover a coluna aninhada
joined_df = joined_df.drop("idioma_falado_filme")

# Renomear colunas desaninhadas, se necessário
renamed_columns = {
    "english_name": "nome_ingles_filme",
    "name": "nome_idioma_filme",
    "iso_639_1": "sigla_idioma_filme"
}
for old_name, new_name in renamed_columns.items():
    joined_df = joined_df.withColumnRenamed(old_name, new_name)

# Escrever o resultado em parquet
joined_df.write.mode("overwrite").parquet(target_path)

job.commit()





