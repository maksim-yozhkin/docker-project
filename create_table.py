import psycopg2
from psycopg2 import OperationalError

def create_connection(db_name, db_user,db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database = db_name,
            user = db_user,
            password = db_password,
            host = db_host,
            port = db_port,
        )
        print("Підключення до бази даних PostgreSQL виконано успішно!")
    except OperationalError as e:
        print(f"Під час підключення до бази даних PostgreSQL виникла помилка: {e}")
    return connection
def create_table(connection,query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Запит виконано успішно.")
    except OperationalError as e:
        print(f"При виконанні поточного запиту виникла помилка: {e}")
    finally:
        cursor.close()
connection = create_connection("RepairLocDepot","YozhkinMaks","Yozhkin24012003", "127.0.0.1", "5432")
query_create_table1 = """
CREATE TABLE IF NOT EXISTS locomotives (
reg_number SERIAL PRIMARY KEY,
reg_depo VARCHAR(10) NOT NULL,
type VARCHAR(30) NOT NULL,
year_prod DATE DEFAULT CURRENT_DATE NOT NULL
)
"""
query_create_table2 = r"""
CREATE TABLE IF NOT EXISTS brigades (
number_brigade SERIAL PRIMARY KEY,
number_phone VARCHAR(20) CHECK (number_phone ~ '^\+38\(\d{3}\)-\d{3}-\d{2}-\d{2}$') NOT NULL
)
"""
query_create_table3 = """
CREATE TABLE IF NOT EXISTS repairs (
code SERIAL PRIMARY KEY,
reg_num_loc INTEGER REFERENCES locomotives(reg_number),
type VARCHAR(30) NOT NULL,
date_start DATE DEFAULT CURRENT_DATE NOT NULL,
needed_days INTEGER NOT NULL,
cost_one_day MONEY DEFAULT 0.0 NOT NULL,
number_brigade INTEGER REFERENCES brigades(number_brigade)
)
"""
query_create_table4= """
CREATE TABLE IF NOT EXISTS workers (
code_worker SERIAL PRIMARY KEY,
surname VARCHAR(30) NOT NULL,
name VARCHAR(30) NOT NULL,
patronymic VARCHAR(20) NOT NULL,
number_brigade INTEGER REFERENCES brigades(number_brigade),
brigadier BOOLEAN DEFAULT FALSE NOT NULL,
date_birth DATE DEFAULT '1900-01-01' NOT NULL
)
"""
create_table(connection,query_create_table1)
create_table(connection,query_create_table2)
create_table(connection,query_create_table3)
create_table(connection,query_create_table4)
connection.close()