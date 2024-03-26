def digit_in_infinity(digit):
    if digit >=0:
        if digit % 2 == 0:
            print(f'Число {digit} прошло проверку и кратно 2')
        elif digit % 3 == 0:
            print(f'Число {digit} прошло проверку и кратно 3')
        elif digit % 5 == 0:
            print(f'Число {digit} прошло проверку и кратно 5')          
        else:
            print(f'Число {digit} не прошло проверку на кратность')

def index_of_word(strr):
    len_s = len(strr)
    print(f'Длина слова {len_s}')
    print('*' * 20)
    for i in range(len_s):
        print(strr[i])
        print(strr[i:])
        print(strr[i::2])

def matrix_unpack():
    A=[[1,2,3],[4,5,6],[7,8,9]]
    res = 0
    for a in A:
        res_sublist = 1
        for elem in a:
            res_sublist *= elem
        res_sublist *= len(a)
        res += res_sublist
    res *= len(A)
    print(f'Результат: {res}')
    

if __name__ == '__main__':
    #не добавлял проверки ввода чтобы не загромождать код
    digit = int(input('Введите число: ').strip())
    digit_in_infinity(digit)
    print(20*'*')
    strr = input('Введите слово: ').strip()
    index_of_word(strr)
    print(20*'*')
    matrix_unpack()



