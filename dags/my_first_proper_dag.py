from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
import logging


def my_first_task():
    logger = logging.getLogger("airflow.task")
    logger.addHandler(logging.FileHandler("/tmp/my_first_task.log"))
    logger.info("My first task is running.")

default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": 60,  # Retry delay in seconds
}


dag = DAG(
    dag_id="my_first_proper_dag",
    default_args=default_args,
    description="A simple DAG to demonstrate logging",
    schedule=None,  # Set to None for manual triggering
    start_date=None,  # Use the default start date
)
my_first_task_operator = PythonOperator(
    task_id="my_first_task",
    python_callable=my_first_task,
    dag=dag,
)