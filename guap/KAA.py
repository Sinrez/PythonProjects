def cesar_main(message, step):
    alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    result = ''    #создаем переменную для вывода итогового сообщения
    for charr in message:
        alfavit = alfavit_RU if charr.upper() in alfavit_RU else alfavit_EU
        position = alfavit.find(charr.upper()) #Вычисляем текущее место символа в списке
        new_position = (position + step) % len(alfavit)    
        #Сдвигаем символы на указанный в переменной step шаг, 
        #% добавлty чтобы последне буквы алфавита сдвигались на первые
        if charr in alfavit:
                result += alfavit[new_position]  # Задаем значения в итог
        elif not charr.isupper() and charr.upper() in alfavit: 
                #Если буква не прописная, то приводим к прописной и проверяем наличие в алфавите
                result += alfavit[new_position].lower()
                #нашли, то добавляем
        else:
                result += charr
    return result

if __name__ == '__main__':
    try:
        step = int(input('Шаг шифровки: ').strip())   #Создаем переменную с шагом шифровки
        message = input("Сообщение для шифровки: ").strip()   #создаем переменнную, куда запишем наше сообщение
        print(f'Зашифровано: {cesar_main(message, step)}')
    except ValueError as ve:
        print(f'Лэ число шагов должно быть числом! {ve}')
    except Exception as ex:
        print(f'Случилась ошибка: {ex}')    
