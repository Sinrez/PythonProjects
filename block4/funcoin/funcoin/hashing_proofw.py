from random import randint

def check_proof_of_work(input_text):
    my_hash = hash(input_text)
    my_int_hash = int(my_hash) + randint(1, 100500)
    if my_int_hash > 100000:
        print('Ошибка, не пройдена проверка!')
    else:
        print(my_int_hash)

if __name__ == '__main__':
    check_proof_of_work('Заходи не бойся, выходи не плачь')
    check_proof_of_work('Квинтэссенция науки')