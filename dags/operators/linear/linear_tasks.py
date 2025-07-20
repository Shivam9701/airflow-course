from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime

def task(name):
    def _task():
        print(f"Task #{name} running at your service sir.")
    
    return _task


with DAG(
    "basic_linear_dag",
    description="A linear Dag",
    start_date=datetime(2025, 6, 14),
    schedule="@weekly"
) as dag:
    task_1 = PythonOperator(task_id="task_1", python_callable=task("1"))
    task_2 = PythonOperator(task_id="task_2", python_callable=task("2"))
    task_3 = PythonOperator(task_id="task_3", python_callable=task("3"))
    
    task_1 >> task_2 >> task_3