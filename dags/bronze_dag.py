from datetime import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.utils.task_group import TaskGroup

with DAG(
    dag_id="kineticlake_bronze",
    start_date=datetime(2026, 6, 16),
    schedule_interval=None,
    catchup=False,
) as dag:
    start = EmptyOperator(task_id="start")

    # Parallel tasks for each Bronze table
    with TaskGroup("bronze_tables") as bronze_tables:
        bronze_imu = EmptyOperator(task_id="bronze_imu_data")
        bronze_encoder = EmptyOperator(task_id="bronze_encoder_data")
        bronze_gps = EmptyOperator(task_id="bronze_gps_data")

    end = EmptyOperator(task_id="end")

    start >> bronze_tables >> end
