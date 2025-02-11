from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.amazon.aws.sensors.s3_key import S3KeySensor


default_args = {
    'owner': 'coder2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=10)
}


with DAG(
    dag_id='dag_with_minio_s3_v02',
    start_date=datetime(2025, 2, 7),
    schedule_interval='@daily',
    default_args=default_args
) as dag:
    task1 = S3KeySensor(
    task_id='sensor_minio_s3',
    bucket_name='airflow',
    bucket_key='data.csv',
    aws_conn_id='minio_conn',
    mode='poke',
    poke_interval=30,  # هر 30 ثانیه چک کند
    timeout=600  # 10 دقیقه صبر کند
)