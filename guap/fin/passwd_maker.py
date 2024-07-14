import string
import random
import tkinter as tk
from tkinter import ttk
import os

# Путь к файлу для сохранения паролей
PASSWORD_FILE = "passwords.txt"

def generate_password():
    """Генерирует случайный пароль длиной 12 символов"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(12))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def check_password():
    """Проверяет, соответствует ли введенный пароль требованиям"""
    password = password_entry.get()
    if len(password) < 8:
        result_label.config(text="Пароль должен быть длиной не менее 8 символов", background="red")
    elif not any(char.isupper() for char in password):
        result_label.config(text="Пароль должен содержать хотя бы одну заглавную букву", background="red")
    elif not any(char.isdigit() for char in password):
        result_label.config(text="Пароль должен содержать хотя бы одну цифру", background="red")
    else:
        result_label.config(text="Пароль соответствует требованиям", background="green")
        save_password(password)

def save_password(password):
    """Сохраняет пароль в файл"""
    if os.path.exists(PASSWORD_FILE):
        mode = "a"  # Дозаписываем в существующий файл
    else:
        mode = "w"  # Создаем новый файл
    with open(PASSWORD_FILE, mode) as file:
        file.write(password + "\n")
    result_label.config(text="Пароль сохранен", background="green")

# Создание окна приложения
root = tk.Tk()
root.title("Генератор и проверка паролей")

# Создание элементов интерфейса
password_label = ttk.Label(root, text="Сгенерированный пароль:")
password_label.grid(row=0, column=0, padx=10, pady=10)

password_entry = ttk.Entry(root)
password_entry.grid(row=0, column=1, padx=10, pady=10)

generate_button = ttk.Button(root, text="Сгенерировать", command=generate_password)
generate_button.grid(row=1, column=0, padx=10, pady=10)

check_button = ttk.Button(root, text="Проверить", command=check_password)
check_button.grid(row=1, column=1, padx=10, pady=10)

result_label = ttk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Запуск главного цикла
root.mainloop()