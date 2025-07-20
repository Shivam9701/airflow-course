from airflow import DAG
from airflow.providers.standard.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.providers.standard.operators.empty import EmptyOperator

with DAG(dag_id="trigger_dag_parent", schedule=None, tags=["trigger", "parent"]) as dag:
    start = EmptyOperator(task_id="start")
    child_dag = TriggerDagRunOperator(
        task_id="trigger_child",
        trigger_dag_id="trigger_dagrun_child",
        wait_for_completion=True,
        reset_dag_run=True,
    )

    start >> child_dag >> EmptyOperator(task_id="finish")
