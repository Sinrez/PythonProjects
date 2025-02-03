def atbash(mode: int, strr: str, alf: str) -> str:
    """Функция реализует шифр Атбаш"""
    spec_symb = ' .,;:!?—()[]{}<>«»‘’“”'
    res = {}
    if mode == 0:
        res = {alf[i]: alf[::-1][i] for i in range(len(alf))}
        #шифрование: первой букве алфавита сопоставлена последняя, второй – на предпоследняя и т. д.  
    elif mode == 1:
        #расшифрование: последней букве алфавита сопоставлена первая, предпоследней – на вторая и т. д.  
        res = {alf[::-1][i]: alf[i] for i in range(len(alf))}
    for s in strr:
        # Проверяем наличие символов в алфавите и пропускаем знаки препинания 
        if s not in spec_symb and s.lower() not in alf:
            return 'Такой буквы нет в алфавите!'
    # Шифруем или расшифровываем
    return ''.join([res.get(s, s) for s in strr])

if __name__ == '__main__':
    import string 
    eng_alph = ''.join(list(string.ascii_lowercase))
    rus_alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    try:
        input_mode = int(input('Введите 0 - шифровать, 1 - если расшифровать: ').strip())
        input_alph = int(input('Выберите язык: 0 - Русский, 1 - Английский: ').strip())
        input_string = input('Введите текст для шифровки: ').strip().lower()
    except ValueError as ve:
        exit(f'Введена не цифра: {ve}')
    except Exception as ex:
        exit(f'Случилась другая ошибка: {ex}')

    if input_alph == 0:
        alph = rus_alph
        print('*' * 50)
        print('Выбран русский алфавит для шифрования')
    elif input_alph == 1:
        alph = eng_alph
        print('*' * 50)
        print('Выбран английский алфавит для шифрования')
    else:
        print('Некорректный выбор языка!')
        exit()

    print(f'Исходный текст: {input_string}')
    print(f'Зашифровано: {atbash(input_mode, input_string, alph)}')
    print('*' * 50)