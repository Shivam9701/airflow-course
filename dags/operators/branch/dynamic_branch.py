from airflow import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.python import (
    PythonOperator,
    BranchPythonOperator,
)
from datetime import datetime

regions = ["us", "eu", "apac", "latam", "india"]


def choose_regions():
    import random

    # Simulate selecting any random subset of regions
    selected = random.sample(regions, k=random.randint(1, len(regions)))
    print(f"Selected regions: {selected}")
    return [f"process_{region}" for region in selected]


with DAG(
    dag_id="dynamic_branching_dag",
    start_date=datetime(2023, 1, 1),
    schedule=None,
    catchup=False,
    tags=["branching", "dynamic"],
) as dag:

    start = EmptyOperator(task_id="start")

    branch = BranchPythonOperator(
        task_id="branch_by_region",
        python_callable=choose_regions,
    )

    region_tasks = []
    for region in regions:
        t = PythonOperator(
            task_id=f"process_{region}",
            python_callable=lambda r=region: print(f"Processing data for {r}"),
        )
        region_tasks.append(t)

    join = PythonOperator(
        task_id="final_merge_task",
        python_callable=lambda: print("Merging data after selected regions."),
        trigger_rule="none_failed_min_one_success",
    )

    end = EmptyOperator(task_id="end")

    # DAG Structure
    start >> branch
    for t in region_tasks:
        branch >> t >> join
    join >> end
