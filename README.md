# Fraud Detection ETL Pipeline 🚀

## Overview
An end-to-end Data Engineering pipeline that detects credit card fraud using Big Data technologies.

## Tech Stack
- **HDFS** — Distributed storage for raw data
- **Apache Spark 3.4.1** — Data processing and transformation
- **YARN** — Resource management
- **Snowflake** — Data Warehouse (DWH)
- **Apache Airflow** — Pipeline orchestration

## Dataset
- **Source:** Credit Card Transactions Fraud Detection
- **Size:** 1,296,675 transactions
- **Fraud Rate:** 0.58% (7,506 fraud cases)

## Star Schema
fact_transactions
├── dim_customer
├── dim_merchant
└── dim_time

## Pipeline Steps
1. Load raw CSV data into HDFS
2. Read data with Spark (YARN as resource manager)
3. Apply transformations and build Star Schema
4. Load final data to Snowflake DWH
5. Orchestrate pipeline with Airflow DAG

## Project Structure
fraud-etl-pipeline/
├── README.md
├── etl/
│   └── fraud_etl.py
├── dags/
│   └── fraud_etl_dag.py
└── sql/
└── create_tables.sql

## Results
| Metric | Value |
|--------|-------|
| Total Transactions | 1,296,675 |
| Fraud Cases | 7,506 |
| Fraud Percentage | 0.58% |