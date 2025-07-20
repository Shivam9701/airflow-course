from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="bash_operator_example",
    start_date=datetime(2024, 1, 1),
    schedule=None,  # Run manually
    catchup=False,
    tags=["bash", "operator", "example"],
) as dag:

    bash_task = BashOperator(
        task_id="print_hello", bash_command="echo 'Hello from BashOperator!'"
    )
