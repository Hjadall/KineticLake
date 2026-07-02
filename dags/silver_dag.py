from datetime import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.utils.task_group import TaskGroup

with DAG(
    dag_id="kineticlake_silver",
    start_date=datetime(2026, 6, 16),
    schedule_interval=None,
    catchup=False,
) as dag:
    start = EmptyOperator(task_id="start")

    # Parallel flows for each Silver SCD2 target
    with TaskGroup("silver_tables") as silver_tables:
        silver_imu = EmptyOperator(task_id="silver_imu_history")
        silver_encoder = EmptyOperator(task_id="silver_encoder_history")
        silver_gps = EmptyOperator(task_id="silver_gps_history")

    end = EmptyOperator(task_id="end")

    start >> silver_tables >> end
