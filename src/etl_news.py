from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, regexp_replace, to_timestamp

def run_etl(input_path, output_path):
    # 1. Initialize Spark
    spark = SparkSession.builder \
        .appName("NewsETLPipeline") \
        .getOrCreate()
    

    # 2. Load raw JSON data (can be local or from S3)
    print("Reading raw data from:", input_path)
    df = spark.read.option("multiline", "true").json(input_path)

    # 3. Basic cleaning and formatting
    df_cleaned = df.withColumn("clean_title", lower(regexp_replace(col("title"), "[^a-zA-Z0-9 ]", ""))) \
                   .withColumn("clean_description", lower(regexp_replace(col("description"), "[^a-zA-Z0-9 ]", ""))) \
                   .withColumn("publishedAt", to_timestamp("publishedAt"))

    # 4. Filter out records with missing dates
    df_cleaned = df_cleaned.filter(col("publishedAt").isNotNull())

    # 5. Write cleaned data to output (Parquet format)
    df_cleaned.write.mode("overwrite").parquet(output_path)

    spark.stop()
    print(f"✅ ETL complete. Cleaned data saved to: {output_path}")

if __name__ == "__main__":
    dir = "/home/divij/work"
    run_etl(f"{dir}/data/raw_news.json", f"{dir}/output/cleaned_news.parquet")