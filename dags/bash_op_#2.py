from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="bash_op_imd",
    schedule=None,
    description="Bash Operator",
    tags=["bash", "operator"],
) as dag:
    date_str = datetime.now().strftime("%Y%m%d")

    create_folder_task = BashOperator(
        task_id="create_folder",
        bash_command=f"mkdir -p ~/airflow-course/date_logs/{date_str}",
    )
    write_log_task = BashOperator(
        task_id="write_log",
        bash_command=f"""\
        echo "hello baby" >> ~/airflow-course/date_logs/{date_str}/logs.log
        """,
    )
    create_folder_task >> write_log_task
