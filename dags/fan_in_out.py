from airflow import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime


# Define a simple Python function for demo purposes
def log_task(msg):
    print(f"Task says: {msg}")


with DAG(
    dag_id="fan_out_fan_in_dag",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["fanout", "fanin", "empty_operator", "operator"],
) as dag:

    # Start marker
    start = EmptyOperator(task_id="start")

    # Three parallel Python tasks
    task1 = PythonOperator(
        task_id="task1",
        python_callable=log_task,
        op_args=["Running Task 1"],
    )

    task2 = PythonOperator(
        task_id="task2",
        python_callable=log_task,
        op_args=["Running Task 2"],
    )

    task3 = PythonOperator(
        task_id="task3",
        python_callable=log_task,
        op_args=["Running Task 3"],
    )

    # Join point after all parallel tasks
    join = EmptyOperator(task_id="join")

    # End marker
    finish = EmptyOperator(task_id="finish")

    # Define the structure
    start >> [task1, task2, task3] >> join >> finish
