from airflow import DAG
from airflow.providers.standard.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.empty import EmptyOperator

import time

with DAG(
    dag_id ='etl_extract_data',
    schedule=None,
    tags=["operator", "trigger"]
) as dag:
    extract_data = \
        BashOperator(
            task_id ='extract_data',
            bash_command=\
                'echo "Extracting Data" > /tmp/user_data.csv'
        )
    print("Data Extracted, now sleeping...")
    time.sleep(2)
    transform_data = TriggerDagRunOperator(
        task_id = 'transform_data',
        trigger_dag_id='etl_transform_data',
        wait_for_completion=True
    )
    
    extract_data >> transform_data >> EmptyOperator(task_id ='finishh')