from datetime import datetime
from airflow import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

default_args = {"owner": "airflow", "depends_on_past": False}

with DAG(
    dag_id="kineticlake_main",
    default_args=default_args,
    start_date=datetime(2026, 6, 16),
    schedule_interval=None,
    catchup=False,
) as dag:
    trigger_bronze = TriggerDagRunOperator(task_id="trigger_bronze", trigger_dag_id="kineticlake_bronze")

    trigger_silver = TriggerDagRunOperator(task_id="trigger_silver", trigger_dag_id="kineticlake_silver")

    trigger_gold = TriggerDagRunOperator(task_id="trigger_gold", trigger_dag_id="kineticlake_gold")

    # Bronze -> Silver -> Gold
    trigger_bronze >> trigger_silver >> trigger_gold
