from db import get_connection

def create_table(): 
    with get_connection() as conn: 
        with conn.cursor() as cur:
            cur.execute(
                """CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) UNIQUE,
                age INT);""")
    print("table created or was already created")

def insert_value(name, age):
    with get_connection() as conn:
        with conn.cursor() as cur: 
            cur.execute(
            """INSERT INTO users (name, age) VALUES (%s, %s) ON CONFLICT (name) DO UPDATE SET age = EXCLUDED.age;""", (name, age)
        )
    print(f"inserted values: {name}, {age}")

def select_values():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM users")
            return cur.fetchall()

