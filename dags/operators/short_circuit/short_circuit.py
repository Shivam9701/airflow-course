from airflow import DAG
from airflow.providers.standard.operators.python import (
    ShortCircuitOperator,
    PythonOperator,
)
from airflow.providers.standard.operators.empty import EmptyOperator
import os


def file_exist_check():
    return os.path.exists("/tmp/user_data.csv")


def process_file():
    print("Processing file ...")


with DAG(
    dag_id="short_circuit",
    schedule="@daily",
) as dag:
    check_op = ShortCircuitOperator(
        task_id="file_check", python_callable=file_exist_check
    )

    process_op = PythonOperator(task_id="process_file", python_callable=process_file)

    check_op >> process_op >> EmptyOperator(task_id="meh")
