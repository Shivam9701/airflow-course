from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="trigger_dagrun_child",
    start_date=datetime(2025, 7, 1),
    schedule=None,
    tags=["trigger", "child"],
) as dag:

    task = BashOperator(
        task_id="child_task", bash_command="echo 'This is the child DAG running!'"
    )
