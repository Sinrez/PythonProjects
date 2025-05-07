import sqlite3 as sq3
import os
from pprint import pprint

# Удаляем старую базу, если нужно
if os.path.exists("./test_db.db3"):
    os.remove("test_db.db3")

try:
    # Подключаемся к базе
    db_conn = sq3.connect("test_db.db3")
    db_cur = db_conn.cursor()

    # Создаем таблицу
    db_cur.execute("""CREATE TABLE employees (
        id INTEGER,
        last_name TEXT,
        first_name TEXT,
        email TEXT
    )""")

    # Данные для вставки
    list_employees = [
        (1, 'Антиповский', 'Герасим', 'gerasim77@hotmail.com'),
        (2, 'Нилина', 'Ольга', 'olga05101963@gmail.com'),
        (3, 'Машира', 'Римма', 'rimma17021969@ya.ru'),
        (4, 'Царско', 'Марианна', 'marianna1998@gmail.com'),
        (5, 'Фирсов', 'Василий', 'vasiliy1968@rambler.ru'),
        (6, 'Борев', 'Яков', 'yakov1964@gmail.com')
    ]

    # Вставляем данные
    db_cur.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", list_employees)

    # Фиксируем изменения
    db_conn.commit()

    db_cur.execute("SELECT * FROM employees")
    pprint(db_cur.fetchall()) #глянем, че вставилось

except Exception as e:

    # Отмена внесённых изменений если ошибка или сломалась база
    if db_conn : db_conn.rollback()

    print("Ошибка:", e)

# Закрываем соединение шоб наверняка все сохранилось
finally:

    # Закрытие курсора и соединения с базой данных
    if db_conn :
        db_cur.close()
        db_conn.close()
