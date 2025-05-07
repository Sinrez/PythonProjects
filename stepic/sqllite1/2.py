# Импорт модулей
import sqlite3 as sq3
import os

# Удаление файла базы данных, если он существует
if os.path.exists("./test_db.db3"):
    os.remove("test_db.db3")

# Создание базы данных
db_conn = sq3.connect("test_db.db3")

# Создание курсора
db_cur = db_conn.cursor()

# Выполнение SQL-запросов
# Создание таблицы employees
db_cur.execute("""CREATE TABLE employees (
    id INTEGER,
    last_name TEXT,
    first_name TEXT,
    email TEXT
)""")

# 2 запрос: добавление данных в таблицу employeescl
# db_cur.execute("""INSERT INTO employees (id, last_name, first_name, email)
# VALUES (1, 'Антиповский','Герасим', 'gerasim77@hotmail.com'),
#        (2, 'Нилина','Ольга', 'olga05101963@gmail.com'),
#        (3, 'Машира','Римма', 'rimma17021969@ya.ru'),
#        (4, 'Царско','Марианна', 'marianna1998@gmail.com'),
#        (5, 'Фирсов','Василий', 'vasiliy1968@rambler.ru'),
#        (6, 'Борев','Яков', 'yakov1964@gmail.com');""")

# Добавление данных в таблицу employees
db_cur.execute("INSERT INTO employees (id, last_name, first_name, email) VALUES (1, 'Антиповский','Герасим', 'gerasim77@hotmail.com');")
db_cur.execute("INSERT INTO employees (id, last_name, first_name, email) VALUES (2, 'Нилина','Ольга', 'olga05101963@gmail.com');")
db_cur.execute("INSERT INTO employees (id, last_name, first_name, email) VALUES (3, 'Машира','Римма', 'rimma17021969@ya.ru');")
db_cur.execute("INSERT INTO employees (id, last_name, first_name, email) VALUES (4, 'Царско','Марианна', 'marianna1998@gmail.com');")
db_cur.execute("INSERT INTO employees (id, last_name, first_name, email) VALUES (5, 'Фирсов','Василий', 'vasiliy1968@rambler.ru');")
db_cur.execute("INSERT INTO employees (id, last_name, first_name, email) VALUES (6, 'Борев','Яков', 'yakov1964@gmail.com');")