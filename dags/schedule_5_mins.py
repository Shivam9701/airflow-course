from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
import logging
from datetime import datetime


# Logging configuration - (TIMESTAMP, LOG_LEVEL, MESSAGE)
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger("my_logger")
logger.addHandler(logging.StreamHandler())
logger.addHandler(logging.FileHandler("my_dag.log"))


def run_logs():
    logger.info(f"This log was created at {datetime.now()}")


with DAG(
    dag_id="scheduled_5m_dag",
    description="This runs every 5 minutes",
    default_args={
        "owners": "airflow",
        "retries": 2,
    },
    start_date=datetime(2025, 6, 15, 7, 30, 0),
    schedule="*/5 * * * *",
    catchup=False,
) as dag:
    task1 = PythonOperator(task_id="log_msg", python_callable=run_logs)
