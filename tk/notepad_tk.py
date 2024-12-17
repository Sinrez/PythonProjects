import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import font

filetypes = (("text files", "*.txt"), ("all files", "*.*"))


def new_file():
    input_text.delete("1.0", tk.END)
    window.title("Новый документ")


def open_file():
    file = filedialog.askopenfile(
        title="Открыть документ", initialdir="", filetypes=filetypes
    )
    if file:
        input_text.delete("1.0", tk.END)
        input_text.insert("1.0", file.read())
        window.title(file.name)


def save_file():
    file = filedialog.asksaveasfile(
        title="Сохранить документ", initialdir="", defaultextension=".txt"
    )
    if file:
        text = input_text.get("1.0", tk.END)
        file.write(text)
        window.title(file.name)


def exit_notepad():
    window.destroy()


def font_settings():

    def applyFunction():
        f = familyCombo.get()
        s = sizeCombo.get()
        font_choice = font.Font(family=f, size=s)
        input_text.config(font=font_choice)

    font_window = tk.Toplevel()
    font_window.title("Настройки шрифта")
    font_window.geometry("300x200")
    font_window.resizable(False, False)

    family = tk.Label(font_window, text="Семейство шрифтов")
    family.place(x=20, y=20, width=150)
    familyCombo = ttk.Combobox(font_window, values=list(font.families()))
    familyCombo.place(x=20, y=50, width=150)

    size = tk.Label(font_window, text="Размер")
    size.place(x=200, y=20, width=70)
    sizeCombo = ttk.Combobox(font_window, values=list(range(1, 100)))
    sizeCombo.place(x=200, y=50, width=70)

    applyButton = tk.Button(font_window, text="Применить", command=applyFunction)
    applyButton.place(x=100, y=120, width=100)


def color_settings():

    def applyColor():
        fg = fgColorCombo.get()
        bg = bgColorCombo.get()
        input_text.config(bg=bg, fg=fg)

    colors = ["black", "red", "blue", "white", "green", "yellow", "brown"]
    color_window = tk.Toplevel()
    color_window.title("Настройки цветов")
    color_window.geometry("300x200")
    color_window.resizable(False, False)

    fgColor = tk.Label(color_window, text="Цвет текста")
    fgColor.place(x=20, y=20, width=100)
    fgColorCombo = ttk.Combobox(color_window, values=colors)
    fgColorCombo.place(x=20, y=50, width=120)

    bgColor = tk.Label(color_window, text="Цвет фона")
    bgColor.place(x=150, y=20, width=100)
    bgColorCombo = ttk.Combobox(color_window, values=colors)
    bgColorCombo.place(x=150, y=50, width=120)

    applyButton = tk.Button(color_window, text="Применить", command=applyColor)
    applyButton.place(x=100, y=120, width=100)


# Создание главного окна
window = tk.Tk()
window.title("Блокнот")
window.geometry("600x500")

# Создание главного меню
mainMenu = tk.Menu(window)
window.config(menu=mainMenu)

# Меню файл
file_menu = tk.Menu(mainMenu, tearoff=0)
file_menu.add_command(label="Новый", command=new_file)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_command(label="Выход", command=exit_notepad)

# Меню настройки
settings_menu = tk.Menu(mainMenu, tearoff=0)
settings_menu.add_command(label="Шрифты", command=font_settings)
settings_menu.add_command(label="Цвета", command=color_settings)

# Добавляем меню в главное меню
mainMenu.add_cascade(label="Файл", menu=file_menu)
mainMenu.add_cascade(label="Настройки", menu=settings_menu)

# Текстовое поле
input_text = tk.Text(window)
input_text.pack(fill="both", expand=True)

window.mainloop()