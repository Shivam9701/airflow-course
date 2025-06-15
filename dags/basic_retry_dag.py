from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta

def always_fails():
    print("This task fails intentionally!")
    raise Exception("Intentional failure")

default_args = {
    'owner': 'shivam',
    'retries': 3,
    'retry_delay': timedelta(seconds=10),
}

with DAG(
    dag_id='basic_retry_dag',
    default_args=default_args,
    description='Retry logic demo DAG',
    start_date=datetime(2024, 1, 1),
    schedule='@daily',
    catchup=False
) as dag:

    retry_task = PythonOperator(
        task_id='fail_and_retry',
        python_callable=always_fails
    )
