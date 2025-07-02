from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 6, 10),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'iris_data_pipeline',
    default_args=default_args,
    description='Quarterly pipeline for Iris data ingestion, processing and delivery',
    schedule_interval='@quarterly',
    catchup=False
)

ingestion = BashOperator(
    task_id='kafka_ingestion',
    bash_command='python /opt/airflow/dags/kafka_ingestion.py',
    dag=dag
)

processing = BashOperator(
    task_id='spark_processing',
    bash_command='python /opt/airflow/dags/spark_processing.py',
    dag=dag
)

delivery = BashOperator(
    task_id='final_delivery',
    bash_command='python /opt/airflow/dags/final_delivery.py',
    dag=dag
)

backup = BashOperator(
    task_id='data_backup',
    bash_command='python /opt/airflow/dags/data_backup.py',
    dag=dag
)

# Set task dependencies
ingestion >> processing >> delivery >> backup
