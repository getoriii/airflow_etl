import psycopg

def get_connection():
    return psycopg.connect(
    host="postgres",
    port="5432",
    user="airflow",
    password="airflow",
    dbname="airflow"
    )