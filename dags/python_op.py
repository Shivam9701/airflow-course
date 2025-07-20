from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime


def greet_person(name, city):
    print(
        f"Hello {name}, from {city} today the date is {datetime.date(datetime.now())}"
    )


with DAG(
    "python_op_dag",
    "Simple Python Operator DAG",
    tags=["python", "operator"],
    default_args={
        "owner": "airflow",
        "retries": 2,
    },
    schedule="*/10 * * * *",
    catchup=False,
    start_date=datetime(2025, 6, 19),
) as dag:
    greet_task = PythonOperator(
        task_id="greet_person",
        python_callable=greet_person,
        op_kwargs={"name": "Mr. Lulu", "city": "Islamabad"},
    )
