def caesar_cipher(text, shift, action, alphabet):
    result = ""
    for char in text:
        if char in alphabet:
            shift_amount = shift if action == "Encrypt" else -shift
            shifted_index = (alphabet.index(char) + shift_amount) % len(alphabet)
            result += alphabet[shifted_index]
        else:
            result += char
    return result

russian_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

import tkinter as tk

def submit():
    action = action_var.get()
    shift_value = shift_entry.get()

    try:
        shift = int(shift_value)
        message = message_entry.get()
        result = caesar_cipher(message, shift, action, russian_alphabet)
        result_label.config(text="Result: " + result)
    except ValueError:
        result_label.config(text="Error: Пожалуйста введите корректное значение сдвига!")

# Создание графического интерфейса
root = tk.Tk()
root.title("Шифр Цезаря для русского алфавита")
root.geometry("400x200")  # Размер окна 600x400 пикселей

action_var = tk.StringVar()
action_var.set("Encrypt")

action_label = tk.Label(root, text="Выберите действие:")
action_label.pack()

encrypt_radio = tk.Radiobutton(root, text="Расшифровать", variable=action_var, value="Encrypt")
encrypt_radio.pack()
decrypt_radio = tk.Radiobutton(root, text="Зашифровать", variable=action_var, value="Decrypt")
decrypt_radio.pack()

shift_label = tk.Label(root, text="Введите сдвиг:")
shift_label.pack()
shift_entry = tk.Entry(root)
shift_entry.pack()

message_label = tk.Label(root, text="Введите сообщение:")
message_label.pack()
message_entry = tk.Entry(root)
message_entry.pack()

submit_button = tk.Button(root, text="Выполнить", command=submit)
submit_button.pack()

result_label = tk.Label(root, text="Результат:")
result_label.pack()

root.mainloop()