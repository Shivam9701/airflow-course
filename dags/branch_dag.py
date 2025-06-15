from airflow import DAG
from airflow.providers.standard.operators.python import BranchPythonOperator
from airflow.providers.standard.operators.empty import EmptyOperator
from datetime import datetime
import random

def choose_branch():
    return 'path_a' if random.random() < 0.5 else 'path_b'

with DAG(
    dag_id='branching_dag',
    start_date=datetime(2024, 1, 1),
    schedule='@daily'
) as dag:

    start = BranchPythonOperator(
        task_id='branch_decision',
        python_callable=choose_branch
    )

    path_a = EmptyOperator(task_id='path_a')
    path_b = EmptyOperator(task_id='path_b')
    end = EmptyOperator(task_id='end', trigger_rule='none_failed_min_one_success')

    start >> [path_a, path_b] >> end
