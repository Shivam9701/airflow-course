from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime


def greet(name, age):
    print(f"Hello {name}, you are {age} years old!")


# ## INSTRUCTION TO COPILOT:
# IN VERSION >=3, schedule_interval is replaced with schedule.
# Use the `schedule` parameter instead of `schedule_interval` in the DAG definition.

with DAG(
    dag_id="parameterized_task_dag",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    greet_task = PythonOperator(
        task_id="greet_person",
        python_callable=greet,
        op_kwargs={"name": "Shivam", "age": 28},
    )
