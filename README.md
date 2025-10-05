# social-media-sentiment-pipeline-hive
Big Data pipeline for analyzing social media sentiment using PySpark, VADER, and Hive.
# 🧠 Social Media Sentiment Analysis — Batch Processing Pipeline (Hive Edition)

A **Big Data batch processing pipeline** built with **Apache Spark (PySpark)** and **Hive** to perform **sentiment analysis** on large volumes of social media posts (tweets, comments, or other text data).  
This project showcases distributed batch data processing, NLP-based sentiment analysis, and Hive-based data warehousing for analytical reporting.

---

## 🚀 Features

- Ingests large datasets from **HDFS**, **AWS S3**, or local file systems  
- Cleans and processes unstructured text data  
- Performs **sentiment classification** (Positive, Neutral, Negative) using **NLTK VADER**  
- Stores processed and aggregated data in **Hive tables** for analysis  
- Generates **daily sentiment summary reports**  
- Demonstrates a scalable **ETL + NLP + Hive** pipeline in Spark

---

## 🧰 Tech Stack

| Component | Purpose |
|------------|----------|
| **Apache Spark (PySpark)** | Distributed data processing |
| **Hive / HDFS** | Data warehousing and storage |
| **Python 3.8+** | Language for the Spark job |
| **NLTK (VADER)** | Sentiment analysis |
| **AWS S3 (optional)** | Cloud-based data input/output |

---

## ⚙️ Setup Instructions

### 1️⃣ Install dependencies
Make sure you have Python and Spark installed, then run:
```bash
pip install -r requirements.txt
