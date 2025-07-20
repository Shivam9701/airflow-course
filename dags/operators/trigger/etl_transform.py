from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator


def transform_data():
    with open("/tmp/user_data.csv", "r") as f:
        data = f.read()
        with open("/tmp/data_transformed.csv", "w") as fw:
            fw.write(f"{data}\ntransformed: yes")


with DAG(
    dag_id="etl_transform_data", schedule=None, tags=["operator", "trigger"]
) as dag:
    transform_task = PythonOperator(
        task_id="etl_transform", python_callable=transform_data
    )
