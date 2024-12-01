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
            options="-c client_encoding=UTF8"
        )
        print("Підключення до бази даних PostgreSQL виконано успішно!")
    except OperationalError as e:
        print(f"Під час підключення до бази даних PostgreSQL виникла помилка: {e}")
    return connection
def insert_table(connection,query,data):
    cursor = connection.cursor()
    try:
        cursor.execute(query,data)
        connection.commit()
        print("Запит виконано успішно.")
    except OperationalError as e:
        print(f"При виконанні поточного запиту виникла помилка: {e}")
    finally:
        cursor.close()

connection = create_connection("RepairLocDepot","YozhkinMaks","Yozhkin24012003", "localhost", "5432")
locomotives = [
    ("Фастів","Вантажний","2021-05-23"),
    ("Козятин","Пасажирський","2020-02-02"),
    ("Козятин","Пасажирський","2024-08-11"),
    ("П'ятихатки","Вантажний","2017-04-29"),
    ("Фастів","Вантажний","2019-01-15"),
    ("П'ятихатки","Пасажирський","2021-06-21"),
    ("П'ятихатки","Пасажирський","2021-12-03"),
    ("Козятин","Вантажний","2024-09-25"),
    ("Фастів","Пасажирський","2023-10-19")
]
brigades = [
    ("+38(068)-433-02-43",),
    ("+38(093)-126-32-95",),
    ("+38(067)-789-56-87",)
]
repairs = [
    (8,"Технічне обслуговування", "2024-04-08", 10, 4350000, 2),
    (5,"Технічне обслуговування", "2024-06-12", 18, 4134000, 2),
    (4,"Позаплановий", "2024-03-11", 12, 5380000, 1),
    (1,"Поточний", "2024-01-08", 24, 6150000, 3),
    (6,"Поточний", "2024-02-28", 15, 5819000, 1),
    (7,"Технічне обслуговування", "2024-05-22", 24, 4356000, 2),
    (7,"Позаплановий", "2024-07-01", 14, 5467000, 3),
    (9,"Технічне обслуговування", "2024-09-13", 20, 4544000, 1),
    (3,"Технічне обслуговування", "2024-11-18", 15, 4937000, 2),
    (2,"Позаплановий", "2024-07-05", 10, 5678000, 2),
    (3,"Поточний", "2024-06-26", 13, 6056000, 3)
]
workers = [
    ("Пасенюк","Златодан","Макарович",1,False,"1990-05-25"),
    ("Повх","Фауст","Соломонович",2,False,"1992-07-04"),
    ("Іщак","Шарлота","Зорянівна",2,True,"1986-02-11"),
    ("Їжак","Огняна","Милославівна",3,False,"1994-11-22"),
    ("Юрженко","Юрій","Адріанович",3,False,"1979-03-18"),
    ("Теліженко","Магадар","Тихонович",1,True,"1982-06-24"),
    ("Озаркевич","Тимофій","Пилипович",2,False,"1991-12-06"),
    ("Юркевич","Йосип","Ігорович",3,True,"1984-05-19"),
    ("Довженко","Єгор","Драганович",1,False,"1990-10-30")
]
loc_join = ", ".join(["%s"]*len(locomotives))
brigad_join = ", ".join(["%s"]*len(brigades))
rep_join = ", ".join(["%s"]*len(repairs))
work_join = ", ".join(["%s"]*len(workers))
query_insert_table1 = (
    f"INSERT INTO locomotives (reg_depo,type,year_prod) VALUES {loc_join}"
)
query_insert_table2 = (
    f"INSERT INTO brigades (number_phone) VALUES {brigad_join}"
)
query_insert_table3 = (
    f"INSERT INTO repairs (reg_num_loc,type,date_start,needed_days,cost_one_day,number_brigade) VALUES {rep_join}"
)
query_insert_table4 = (
    f"INSERT INTO workers (surname,name,patronymic,number_brigade,brigadier,date_birth) VALUES {work_join}"
)
insert_table(connection,query_insert_table1,locomotives)
insert_table(connection,query_insert_table2,brigades)
insert_table(connection,query_insert_table3,repairs)
insert_table(connection,query_insert_table4,workers)
connection.close()