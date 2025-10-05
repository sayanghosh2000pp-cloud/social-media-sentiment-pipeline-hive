import argparse
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col, to_date, expr
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

from sentiment import analyze_text
from utils import clean_text

def sentiment_udf():
    from pyspark.sql.types import StructType, StructField, DoubleType, StringType
    schema = StructType([
        StructField('compound', DoubleType()),
        StructField('pos', DoubleType()),
        StructField('neu', DoubleType()),
        StructField('neg', DoubleType()),
        StructField('label', StringType()),
    ])

    def _inner(text):
        try:
            return analyze_text(text)
        except Exception:
            return (0.0, 0.0, 0.0, 0.0, 'neutral')

    return udf(_inner, schema)

def main(args):
    spark = SparkSession.builder.appName('social-media-sentiment-batch').enableHiveSupport().getOrCreate()

    input_path = args.input
    if input_path.endswith('.json') or input_path.endswith('.jsonl') or input_path.endswith('.ndjson'):
        df = spark.read.json(input_path)
    else:
        df = spark.read.option('header', True).csv(input_path)

    possible_text_cols = ['text', 'content', 'tweet', 'message']
    for c in possible_text_cols:
        if c in df.columns:
            text_col = c
            break
    else:
        text_col = df.columns[0]

    if 'created_at' in df.columns:
        ts_col = 'created_at'
    else:
        ts_col = 'timestamp' if 'timestamp' in df.columns else None

    clean_udf = udf(lambda s: clean_text(s), StringType())
    df2 = df.withColumn('clean_text', clean_udf(col(text_col)))

    s_udf = sentiment_udf()
    df3 = df2.withColumn('sent', s_udf(col('clean_text')))

    df4 = (
        df3
        .withColumn('sent_compound', col('sent.compound'))
        .withColumn('sent_pos', col('sent.pos'))
        .withColumn('sent_neu', col('sent.neu'))
        .withColumn('sent_neg', col('sent.neg'))
        .withColumn('sent_label', col('sent.label'))
    )

    if ts_col:
        df4 = df4.withColumn('created_date', to_date(col(ts_col)))
    else:
        df4 = df4.withColumn('created_date', expr("current_date()"))

    spark.sql("CREATE DATABASE IF NOT EXISTS sentiment_db")
    df4.write.saveAsTable('sentiment_db.raw_sentiment', mode='overwrite')

    summary = df4.groupBy('created_date', 'sent_label').count()
    pivot = summary.groupBy('created_date').pivot('sent_label', ['positive', 'neutral', 'negative']).sum('count')
    agg = df4.groupBy('created_date').agg({'sent_compound': 'avg', '*': 'count'})
    agg = agg.join(pivot, on='created_date', how='left')

    summary_out = args.output.rstrip('/') + '/summary'
    agg.coalesce(1).write.mode('overwrite').option('header', True).csv(summary_out)

    spark.stop()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--mode', choices=['parquet', 'hive'], default='hive')
    args = parser.parse_args()
    main(args)
