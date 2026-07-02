from datetime import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="kineticlake_gold",
    start_date=datetime(2026, 6, 16),
    schedule_interval=None,
    catchup=False,
) as dag:
    start = EmptyOperator(task_id="start")

    # Build Gold artifacts in order
    build_gold_master = EmptyOperator(task_id="gold_kinetic_master")
    build_gold_ml = EmptyOperator(task_id="gold_ml_features")

    end = EmptyOperator(task_id="end")

    start >> build_gold_master >> build_gold_ml >> end
