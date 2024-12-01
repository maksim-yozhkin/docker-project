import os
import django

# Ініціалізація Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yozhkindjangoproject.settings')
django.setup()

from django.db import connection

def check_encoding():
    with connection.cursor() as cursor:
        # Змініть `table_name` і `column_name` на ваші
        cursor.execute("SELECT number_brigade FROM brigades;")
        for row in cursor.fetchall():
            try:
                row[0].encode('utf-8').decode('utf-8')
            except UnicodeDecodeError:
                print(f"Некоректне кодування: {row[0]}")

if __name__ == "__main__":
    check_encoding()