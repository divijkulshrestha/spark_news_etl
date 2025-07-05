# spark_news_etl

Goal: A script that turns raw news → clean data.


🔰 STAGE 1: Local MVP (Minimal Viable Product)

This gets the core idea working before adding the cloud.

Steps:

1️⃣	Collect a few news articles	(Use RSS or NewsAPI)

2️⃣	Save them as a JSON file (raw_news.json)

3️⃣	Write and run a local Spark ETL script

4️⃣	Save cleaned results as Parquet

✅ Output: cleaned_news.parquet locally.