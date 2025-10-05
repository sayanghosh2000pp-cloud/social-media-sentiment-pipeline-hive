CREATE DATABASE IF NOT EXISTS sentiment_db;

CREATE EXTERNAL TABLE IF NOT EXISTS sentiment_db.raw_sentiment (
  id STRING,
  user STRING,
  text STRING,
  clean_text STRING,
  created_at TIMESTAMP,
  sent_compound DOUBLE,
  sent_pos DOUBLE,
  sent_neu DOUBLE,
  sent_neg DOUBLE,
  sent_label STRING
)
PARTITIONED BY (created_date DATE)
STORED AS PARQUET
LOCATION '/user/hive/warehouse/sentiment_db/raw_sentiment';

CREATE TABLE IF NOT EXISTS sentiment_db.daily_summary (
  created_date DATE,
  avg_compound DOUBLE,
  total_count BIGINT,
  positive BIGINT,
  neutral BIGINT,
  negative BIGINT
)
STORED AS PARQUET;
