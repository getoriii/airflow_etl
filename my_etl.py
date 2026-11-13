from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime
from logic import create_table, insert_value, select_values

def create_table_task():
    print("--- НАЧАЛО РАБОТЫ ---")
    create_table()
    insert_value("John Doe", 30)
    data = select_values()
    print(f"Данные в базе: {data}")
    print("--- КОНЕЦ РАБОТЫ ---")
try:
    with DAG(
        dag_id="basic_etl_dag",
        start_date=datetime(2026, 1, 1),
        schedule="@hourly",
        end_date=datetime(2026, 2, 1),
        catchup=False
    ) as dag:

        task = PythonOperator(
            task_id="create_table",
            python_callable=create_table_task
        )
except Exception as e:
    print(f"Ошибка при создании DAG: {e}") #внесение изменения в код для отладки ошибок при создании DAG