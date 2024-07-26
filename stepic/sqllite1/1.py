# Импорт модулей
import sqlite3 as sq3
import os

# Удаление файла базы данных, если он существует
if os.path.exists("./test_db.db3"):
    os.remove("test_db.db3")

# Создание базы данных
with sq3.connect("test_db.db3") as db_conn:
    pass