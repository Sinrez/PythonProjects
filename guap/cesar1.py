alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def cesar_main(message, alfavit, step):
    result = ''    #создаем переменную для вывода итогового сообщения
    for charr in message:
        position = alfavit.find(charr)    #Вычисляем текущее место символа в списке
        new_position = position + step    #Сдвигаем символы на указанный в переменной step шаг
        if charr in alfavit:
                result += alfavit[new_position]  # Задаем значения в итог
        elif not charr.isupper() and charr.upper() in alfavit: 
                #Если буква не прописная, то приводим к прописной и проверяем наличие в алфавите
                result += alfavit[new_position].lower()
                #нашли, то добавляем
        else:
                result += charr
    print(result)

if __name__ == '__main__':
    step = int(input('Шаг шифровки: ').strip())   #Создаем переменную с шагом шифровки
    message = input("Сообщение для шифровки: ").strip()   #создаем переменнную, куда запишем наше сообщение
    lang = input('Выберите язык RU/EU: ')   #Добавляем возможность выбора языка
    if lang == 'RU':
        cesar_main(message, alfavit_RU, step)
    elif lang == 'EU':
        cesar_main(message, alfavit_EU, step)
