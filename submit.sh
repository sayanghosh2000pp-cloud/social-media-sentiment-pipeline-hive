#!/usr/bin/env bash
set -euo pipefail

INPUT=${1:-"s3://my-bucket/raw/social/*.json"}
OUTPUT=${2:-"s3://my-bucket/processed/sentiment"}
MODE=${3:-hive}

spark-submit \      --master yarn \      --deploy-mode cluster \      --conf spark.sql.catalogImplementation=hive \      --conf spark.driver.memory=4g \      --conf spark.executor.memory=4g \      --conf spark.sql.shuffle.partitions=200 \      spark/job.py --input ${INPUT} --output ${OUTPUT} --mode ${MODE}
