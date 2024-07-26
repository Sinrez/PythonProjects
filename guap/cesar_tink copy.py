import tkinter as tk

def caesar_cipher(text, shift, action):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if action == "Encrypt" else -shift
            shifted_char = chr((ord(char) - ord('a' if char.islower() else 'A') + shift_amount) % 26 + ord('a' if char.islower() else 'A'))
            result += shifted_char
        else:
            result += char
    return result

def submit():
    action = action_var.get()
    shift_value = shift_entry.get()

    try:
        shift = int(shift_value)
        message = message_entry.get()
        result = caesar_cipher(message, shift, action)
        result_label.config(text="Result: " + result)
    except ValueError:
        result_label.config(text="Error: Пожалуйста введите корректное значение сдвига!")

# Создание графического интерфейса
root = tk.Tk()
root.title("Caesar Cipher")

action_var = tk.StringVar()
action_var.set("Encrypt")

action_label = tk.Label(root, text="Select Action:")
action_label.pack()

encrypt_radio = tk.Radiobutton(root, text="Encrypt", variable=action_var, value="Encrypt")
encrypt_radio.pack()
decrypt_radio = tk.Radiobutton(root, text="Decrypt", variable=action_var, value="Decrypt")
decrypt_radio.pack()

shift_label = tk.Label(root, text="Enter Shift:")
shift_label.pack()
shift_entry = tk.Entry(root)
shift_entry.pack()

message_label = tk.Label(root, text="Enter Message:")
message_label.pack()
message_entry = tk.Entry(root)
message_entry.pack()

submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

result_label = tk.Label(root, text="Result:")
result_label.pack()

root.mainloop()