CREATE DATABASE IF NOT EXISTS fraud_dwh;
CREATE SCHEMA IF NOT EXISTS fraud_dwh.star_schema;

CREATE TABLE IF NOT EXISTS fraud_dwh.star_schema.dim_customer (
    customer_id BIGINT,
    first STRING,
    last STRING,
    gender STRING,
    street STRING,
    city STRING,
    state STRING,
    zip STRING,
    lat FLOAT,
    long FLOAT,
    city_pop INT,
    dob STRING
);

CREATE TABLE IF NOT EXISTS fraud_dwh.star_schema.dim_merchant (
    merchant_id STRING,
    merchant STRING,
    category STRING,
    merch_lat FLOAT,
    merch_long FLOAT
);

CREATE TABLE IF NOT EXISTS fraud_dwh.star_schema.dim_time (
    trans_datetime STRING,
    hour INT,
    day INT,
    month INT,
    year INT
);

CREATE TABLE IF NOT EXISTS fraud_dwh.star_schema.fact_transactions (
    transaction_id STRING,
    customer_id BIGINT,
    merchant_id STRING,
    trans_datetime STRING,
    amount FLOAT,
    is_fraud INT
);