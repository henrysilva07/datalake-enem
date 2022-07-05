
from pyspark.sql import SparkSession



# Criando minha sessão spark 

spark = (

    SparkSession.builder
            .appName("datalake_enem")
            .getOrCreate()

)


# Lendo os microdados do enem na raw-data

df_enem = (

    spark.read
    .option("header", True)
    .option("inferschema", True)
    .option("delimiter", ";")
    .csv("s3://datalake-henry-enem/raw_data/enem/")

)

# Salvando os dados na stanging zone particionado por ano 

(
    df_enem.write
            .mode("overwrite")
            .format("parquet")
            .partitionBy("NU_ANO")
            .save("s3://datalake-henry-enem/staging/enem")

)