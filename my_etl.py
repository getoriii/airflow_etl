from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta
from logic import create_table, insert_value, select_values

default_args = {
    "owner": "airflow",
    "retries": 3, 
    "retry_delay": timedelta(minutes=5),
    "depend_on_past": False,
    "email_on_failure": False
}

def create_table_task():
    create_table()
    insert_value("John Doe", 30)
    print("--- КОНЕЦ РАБОТЫ ---")
    return 1

def selet_values_task(**context):
    data=select_values()
    inserted_values = context['task_instance'].xcom_pull(task_ids='create_table')
    print(f"Вставленные значения: {inserted_values}")
    print(f"Данные в базе: {data}")
    print("--- КОНЕЦ РАБОТЫ ---")

with DAG(
    dag_id="basic_etl_dag",
    start_date=datetime(2026, 1, 1),
    schedule="@hourly",
    end_date=datetime(2026, 2, 1),
    catchup=False,
    default_args=default_args
    ) as dag:

    task1 = PythonOperator(
        task_id="create_table",
        python_callable=create_table_task
        )
    task2 = PythonOperator(
        task_id="select_values",
        python_callable=select_values_task
        )

task1 >> task2