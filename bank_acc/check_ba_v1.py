
def check_bank_acc(account, bic):
    """Функция вычисления контрольного символа счета, 
    правила тут https://normativ.kontur.ru/document?moduleId=1&documentId=24444"""
    char_dict = { 'A': 0, 'B': 1, 'C': 2, 'E': 3, 'H': 4,'K': 5,'M': 6,'P': 7,'T': 8,'X': 9}
    list_coef = list(map(int, '7,1,3,7,1,3,7,1,3,7,1,3,7,1,3,7,1,3,7,1,3,7,1'.split(',')))
    #было лень искать нормальный формат списка весов))
    curr_key = account[8] #текущий ключевой 9 символ из счета
    bic_bank = bic[-3:] 
    #если буква в счете - заменяем
    # Заменяем буквы на цифры
    acc_without_chars = ''
    for acc in account:
        if acc.upper() in char_dict:
            acc_without_chars += str(char_dict[acc.upper()])
        elif acc.isdigit():
            acc_without_chars += acc
        else:
            raise ValueError("Недопустимый символ в номере счета")
    temp_acc = bic_bank+acc_without_chars[:8]+'0'+acc_without_chars[9:] #обнуление ключевого символа в исходном счете 
 
    summ = 0
    for i in range(23):
        summ += (int(temp_acc[i]) * list_coef[i]) % 10 
        #сумма младших разрядов произведения цифр счета и весов из списка выше (сумма по модулю 10)
    
    control_symbol = (summ % 10 * 3) % 10 
    res = 'верно' if control_symbol == int(curr_key) else 'неверно, проверьте БИК и номер счета'
    print(f'Результат проверки соответствия БИКа {bic} и счета {account}: счет указан {res}')

if __name__ == '__main__':
    print('Функция провреки соответствия БИКа и счета, примеры проверки:')
    print('пример 1')
    check_bank_acc('40802810200000040449', '044525974') #должно быть верно
    print('пример 2')
    check_bank_acc('40602810700000000025', '049805746') #должно быть верно

    try:
        acc = input('Введите номер 20-значный номер счета: ').strip()
        if len(acc) != 20:
            exit('Номер счета должен быть из 20 символов!')
        bic = input('Введите БИК банка: ').strip()
        if len(bic) != 9:
            exit('Размерность БИК - 9 сиволов!')
        for b in bic:
            if b.isalpha():
                exit('Букв не должно быть в БИК')
        check_bank_acc(acc, bic)
    except Exception as ex:
        exit(f'Случилась фигня вида: {ex}')


