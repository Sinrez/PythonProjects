from simple_crypto_utils import keysgen, encrypt, decrypt
import easygui
import os


message = "Выберите необходимое действие"
title = "Simple python rsa_aes"
buttons = ["Инструкция", "Генерация ключей", "Шифрование", "Расшифрование"]
output = easygui.indexbox(message, title, buttons)
restart = "python simple_crypto_gui.py"

if output == 0:
    message = """ВНИМАНИЕ! Разработчик не несет ответственности за любой возможный ущерб 
            в результате использования данного приложения!\n
            Алгоритм действий пользователя
            1. Если Вам необходимо получить информацию задайте имя проекта и сгенерируйте ключевую пару. 
            Файлы сохранятся в папку с приложением (project_name.seprk - закрытый (секретный) ключ и project_name.sepbk - открытый ключ).\n
            2. Любым удобным способом передайте открытый ключ отправляющему пользователю.\n
            3. Отправляющий пользователь зашифровывает необходимый файл (архив) с указанием полученного открытого ключа и любым удобным способом передает его принимающему пользователю.\n
            4. Принимающий пользователь расшифровывает полученный файл с использованием своего закрытого ключа.
            В результате расшифровки формируется файл с расширением '.decrypted', это расширение необходимо удалить и файл будет готов к использованию.\n
            ВАЖНО! Не рекомендуется изменять имена созданных приложением файлов, особенно расширение. Это может повлечь некорректную работу приложения."""
    readme = easygui.msgbox(message, title)
    os.system(restart)
elif output == 1:
    text = "Введите название проекта"
    d_text = "Название проекта"
    prj_name = easygui.enterbox(text, title, d_text)
    keysgen(prj_name)
    message = f"""Ключи для проекта {prj_name} сгенерированы!"""
    ready = easygui.msgbox(message, title)
    os.system(restart)
elif output == 2:
    text1 = 'Выберите файл для шифрования'
    text2 = 'Выберите файл открытого ключа'
    path = easygui.fileopenbox(text1, title)
    pub_key = easygui.fileopenbox(text2, title)
    encrypt(path, pub_key)
    message = f"""Файл {path} зашифрован!"""
    ready = easygui.msgbox(message, title)
    os.system(restart)
elif output == 3:
    text1 = 'Выберите файл для расшифрования'
    text2 = 'Выберите файл закрытого ключа'
    path = easygui.fileopenbox(text1, title)
    sec_key = easygui.fileopenbox(text2, title)
    decrypt(path, sec_key)
    message = f"""Файл {path} расшифрован! Не забудьте удалить окончание '.decrypted' в конце файла"""
    ready = easygui.msgbox(message, title)
    os.system(restart)
else:
    message = f"""Программа завершена!"""
    ready = easygui.msgbox(message, title)



