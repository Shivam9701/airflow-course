from airflow import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.python import (
    PythonOperator,
    BranchPythonOperator,
)
from datetime import datetime
import random


def pick_branch():
    num = random.randint(1, 100)
    print(f"Picked number: {num}")
    return "short_task" if num % 2 == 0 else "long_task_1"


def long_branch_fn(task_name):
    print(f"Running: {task_name}")


with DAG(
    dag_id="branch_unequal_dag",
    start_date=datetime(2023, 1, 1),
    schedule=None,
    catchup=False,
    tags=["branching", "operators", "unequal"],
) as dag:

    start = EmptyOperator(task_id="start")

    branch = BranchPythonOperator(
        task_id="branch_decision", python_callable=pick_branch
    )

    short_task = PythonOperator(
        task_id="short_task",
        python_callable=lambda: print("Short branch task done."),
    )

    long_task_1 = PythonOperator(
        task_id="long_task_1",
        python_callable=lambda: long_branch_fn("long_task_1"),
    )

    long_task_2 = PythonOperator(
        task_id="long_task_2",
        python_callable=lambda: long_branch_fn("long_task_2"),
    )

    long_task_3 = PythonOperator(
        task_id="long_task_3",
        python_callable=lambda: long_branch_fn("long_task_3"),
    )

    final = PythonOperator(
        task_id="final_task",
        python_callable=lambda: print("Final task after branch."),
        trigger_rule="none_failed_min_one_success",
    )

    end = EmptyOperator(task_id="end")

    # DAG structure
    start >> branch

    # short branch
    branch >> short_task >> final

    # long branch
    branch >> long_task_1 >> long_task_2 >> long_task_3 >> final

    final >> end
