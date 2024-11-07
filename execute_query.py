import psycopg2
from psycopg2 import OperationalError
from prettytable import PrettyTable

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
def execute_query(connection,query,parametr):
    cursor = connection.cursor()
    try:
        if parametr == "":
            cursor.execute(query)
        else:
            cursor.execute(query,parametr)
        res_query = cursor.fetchall()
        table = PrettyTable()
        name_columns = []
        for name_column in cursor.description:
            name_columns.append(name_column[0])
        table.field_names = name_columns
        for data_row in res_query:
            table.add_row(data_row)
        print(table)
        print("Запит виконано успішно.")
    except OperationalError as e:
        print(f"При виконанні поточного запиту виникла помилка: {e}")
    finally:
        cursor.close()
connection = create_connection("RepairLocDepot","YozhkinMaks","Yozhkin24012003", "localhost", "5432")
query_1 = "SELECT * FROM locomotives"
query_2 = "SELECT * FROM brigades"
query_3 = "SELECT * FROM repairs"
query_4 = "SELECT * FROM workers"
query_5 = "SELECT * FROM locomotives WHERE type = 'Вантажний' ORDER BY year_prod"
query_6 = ("SELECT code as \"Код ремонту\",reg_num_loc as \"Реєстраційний номер локомотиву\",date_start + INTERVAL '1 days' * needed_days as "
           "\"Кінцева дата ремонту\" FROM repairs")
query_7 = "SELECT number_brigade as \"Номер бригади\",COUNT(code) as \"Кількість ремонтів\" FROM repairs GROUP BY number_brigade"
query_8 = ("SELECT code as \"Код ремонту\",reg_num_loc as \"Реєстраційний номер локомотиву\",cost_one_day * needed_days as "
           "\"Кінцева дата ремонту\" FROM repairs")
query_9 = ("SELECT number_brigade as \"Номер бригади\","
           "COUNT(CASE WHEN type = 'Технічне обслуговування' THEN 1 END) AS \"Технічне обслуговування\","
           "COUNT(CASE WHEN type = 'Поточний' THEN 1 END) AS \"Поточний\","
           "COUNT(CASE WHEN type = 'Позаплановий' THEN 1 END) AS \"Позаплановий\""
           "FROM repairs "
           "GROUP BY number_brigade")
query_10 = "SELECT * FROM locomotives WHERE reg_depo = %s"
execute_query(connection,query_1,"")
execute_query(connection,query_2,"")
execute_query(connection,query_3,"")
execute_query(connection,query_4,"")
execute_query(connection,query_5,"")
execute_query(connection,query_6,"")
execute_query(connection,query_7,"")
execute_query(connection,query_8,"")
execute_query(connection,query_9,"")
parametr_id = input("Введіть назву депо, за якою ви хочете дізнатися приписані до депо локомотиви => ")
execute_query(connection,query_10,(parametr_id,))
connection.close()