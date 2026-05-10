from pyspark.sql import SparkSession
from pyspark.sql.functions import col, hour, dayofmonth, month, year

spark = SparkSession.builder \
    .appName("FraudDetection_ETL") \
    .master("yarn") \
    .config("spark.jars", "/home/teto/spark-snowflake_2.12-2.12.0-spark_3.4.jar,/home/teto/snowflake-jdbc-3.13.30.jar") \
    .getOrCreate()

sfOptions = {
    "sfURL": "fd29437.eu-central-2.aws.snowflakecomputing.com",
    "sfUser": "TAREKWAEL09",
    "sfPassword": "Tarek wael123@",
    "sfDatabase": "fraud_dwh",
    "sfSchema": "star_schema",
    "sfWarehouse": "COMPUTE_WH"
}

SNOWFLAKE_SOURCE = "net.snowflake.spark.snowflake"

df = spark.read.csv("/fraud_project/fraudTrain.csv", header=True, inferSchema=True)

print(f"=== Total Rows: {df.count()} ===")

dim_customer = df.select(
    col("cc_num").alias("customer_id"),
    col("first"), col("last"), col("gender"),
    col("street"), col("city"), col("state"), col("zip"),
    col("lat"), col("long"), col("city_pop"), col("dob")
).dropDuplicates(["customer_id"])

dim_merchant = df.select(
    col("merchant").alias("merchant_id"),
    col("merchant"), col("category"),
    col("merch_lat"), col("merch_long")
).dropDuplicates(["merchant_id"])

dim_time = df.select(
    col("trans_date_trans_time").alias("trans_datetime"),
    hour(col("trans_date_trans_time")).alias("hour"),
    dayofmonth(col("trans_date_trans_time")).alias("day"),
    month(col("trans_date_trans_time")).alias("month"),
    year(col("trans_date_trans_time")).alias("year")
).dropDuplicates(["trans_datetime"])

fact_transactions = df.select(
    col("trans_num").alias("transaction_id"),
    col("cc_num").alias("customer_id"),
    col("merchant").alias("merchant_id"),
    col("trans_date_trans_time").alias("trans_datetime"),
    col("amt").alias("amount"),
    col("is_fraud")
)

def write_to_snowflake(df, table_name):
    df.write \
        .format(SNOWFLAKE_SOURCE) \
        .options(**sfOptions) \
        .option("dbtable", table_name) \
        .mode("overwrite") \
        .save()
    print(f"=== {table_name} saved to Snowflake ✅ ===")

write_to_snowflake(dim_customer, "dim_customer")
write_to_snowflake(dim_merchant, "dim_merchant")
write_to_snowflake(dim_time, "dim_time")
write_to_snowflake(fact_transactions, "fact_transactions")

print("=== All Done! ===")
spark.stop()
