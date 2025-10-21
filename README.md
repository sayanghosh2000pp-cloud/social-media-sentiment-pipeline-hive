# Social Media Sentiment Analysis — Batch Pipeline (Hive Edition)

This project implements a PySpark batch processing pipeline for social media sentiment analysis.
It ingests raw social media data (tweets/posts), cleans text, performs sentiment classification
using NLTK's VADER, and writes results to Hive tables for easy querying.

## Features
- Reads JSON/CSV social media data from HDFS or S3
- Cleans text (removes URLs, mentions, etc.)
- Uses VADER for sentiment scoring
- Stores detailed and aggregated results in Hive tables

## Run Example
```bash
spark-submit spark/job.py --input s3://my-bucket/raw/social/*.json --output /user/hive/warehouse/sentiment_db.db/raw_sentiment --mode hive
```

## Requirements
- Apache Spark 3.x with Hive support
- Hive Metastore configured
- Python 3.8+
