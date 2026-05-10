from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'teto',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='fraud_etl_pipeline',
    default_args=default_args,
    description='ETL Pipeline: HDFS -> Spark -> Snowflake',
    schedule='@daily',
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=['fraud', 'etl', 'spark'],
) as dag:

    start = BashOperator(
        task_id='start',
        bash_command='echo "Starting ETL Pipeline..."',
    )

    check_hdfs = BashOperator(
        task_id='check_hdfs',
        bash_command='hdfs dfs -ls /fraud_project/fraudTrain.csv',
    )

    run_spark_etl = BashOperator(
        task_id='run_spark_etl',
        bash_command='''
        spark-submit \
            --master yarn \
            --jars /home/teto/spark-snowflake_2.12-2.12.0-spark_3.4.jar,/home/teto/snowflake-jdbc-3.13.30.jar \
            --conf spark.driver.extraClassPath=/home/teto/spark-snowflake_2.12-2.12.0-spark_3.4.jar:/home/teto/snowflake-jdbc-3.13.30.jar \
            --conf spark.executor.extraClassPath=/home/teto/spark-snowflake_2.12-2.12.0-spark_3.4.jar:/home/teto/snowflake-jdbc-3.13.30.jar \
            /home/teto/fraud_etl.py
        ''',
    )

    end = BashOperator(
        task_id='end',
        bash_command='echo "ETL Pipeline Completed Successfully!"',
    )

    start >> check_hdfs >> run_spark_etl >> end
