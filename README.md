# Fraud Detection ETL Pipeline 🚀

## Overview
An end-to-end Data Engineering pipeline that detects credit card fraud using Big Data technologies. The pipeline ingests raw transaction data, processes it using Apache Spark, transforms it into a Star Schema, and loads it into Snowflake as a Data Warehouse.

---

## Architecture
![Architecture Diagram](Architecture%20Diagram.png)

---

## Tech Stack
| Tool | Version | Purpose |
|------|---------|---------|
| Apache Hadoop | 3.3.6 | HDFS distributed storage |
| Apache Spark | 3.4.1 | Data processing |
| YARN | 3.3.6 | Resource management |
| Snowflake | — | Data Warehouse |
| Apache Airflow | 2.x | Pipeline orchestration |

---

## Dataset
- **Source:** Credit Card Transactions Fraud Detection (Kaggle)
- **Size:** 1,296,675 transactions
- **Fraud Rate:** 0.58% (7,506 fraud cases)

---

## Star Schema
![Star Schema](Star%20Schema%20Diagram.png)

```
fact_transactions
    ├── dim_customer   (983 unique customers)
    ├── dim_merchant   (693 unique merchants)
    └── dim_time       (1,296,675 time records)
```

---

## Pipeline Steps
1. 📥 **Ingest** — Load raw CSV into HDFS
2. ⚙️ **Process** — Read with Spark (YARN as resource manager)
3. 🔄 **Transform** — Clean data and build Star Schema
4. 📤 **Load** — Push final tables to Snowflake DWH
5. 🕐 **Orchestrate** — Airflow DAG runs daily automatically

---

## Project Structure
```
fraud-etl-pipeline/
├── README.md
├── fraud_etl.py          ← Spark ETL script
├── fraud_etl_dag.py      ← Airflow DAG
├── create_tables.sql     ← Snowflake schema
├── Architecture Diagram.png
└── Star Schema Diagram.png
```

---

## Results
| Metric | Value |
|--------|-------|
| Total Transactions | 1,296,675 |
| Fraud Cases | 7,506 |
| Fraud Percentage | 0.58% |

---

## How to Run

### 1. Start Hadoop & YARN
```bash
start-dfs.sh && start-yarn.sh
```

### 2. Upload data to HDFS
```bash
hdfs dfs -put fraudTrain.csv /fraud_project/
```

### 3. Run Spark ETL
```bash
spark-submit \
  --master yarn \
  --jars spark-snowflake_2.12-2.12.0-spark_3.4.jar,snowflake-jdbc-3.13.30.jar \
  fraud_etl.py
```

### 4. Start Airflow
```bash
airflow standalone &
```
