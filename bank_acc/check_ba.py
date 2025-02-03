
def check_bank_acc(account, bic):
    """Функция вычисления контрольного символа счета"""
    list_coef = list(map(int, '7,1,3,7,1,3,7,1,3,7,1,3,7,1,3,7,1,3,7,1,3,7,1'.split(','))) #было лень искать норм формат коэфф))
    currKey = account[8]
    # bic_rkc = '0'+bic[4:6] ## если передан БИК РКЦ
    bic_bank = bic[-3:]
    # temp_acc = bic_tmp+account[:8]+'0'+account[9:]
    temp_acc = bic_bank+account[:8]+'0'+account[9:]
    
    summ = 0
    for i in range(23):
        summ += (int(temp_acc[i]) * list_coef[i]) % 10
    
    control_symbol = (summ % 10 * 3) % 10
    res = 'верно' if control_symbol == int(currKey) else 'неверно, проверьте БИК и номер счета'

    print(f'Результат проверки соответствия БИКа {bic} и счета {account}: счет указан {res}')

    print(list_coef,'',bic_bank, '', temp_acc, '', summ, '', currKey, '', control_symbol)

if __name__ == '__main__':
    print('пример 1')
    check_bank_acc('40817810800069500276', '044525974') #должно быть верно
    print('пример 2')
    check_bank_acc('40602810700000000025', '049805746') #должно быть верно
    # print('пример 3')
    # check_bank_acc('40102810100000010001', '040305000')