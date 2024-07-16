import hashlib
import time

def check_proof_of_work(input_text, difficulty_bits):
    #задаем целевое значение
    target = 2 ** (256-difficulty_bits)
    start_time = time.time()  # запоминаем время начала поиска
    for nonce in range(1000000):
        input = f'{input_text}{nonce}'.encode()
        my_int_hash = int(hashlib.sha256(input).hexdigest(),16)
        # создаем хеш "число" из данных блока и nonce - некотрого "случайного" значения из большого диапазона чисел
        if my_int_hash < target:
        #проверяем, если полученное число меньше целевого значения
            print(f"Успех с nonce {nonce}")
            print(f"Хеш: {my_int_hash}")
            return (my_int_hash, nonce)
        if time.time() - start_time > 60:  # проверяем, прошла ли минута, ввели ограничение по времни подбора
            print(f"Ошибка, не нашли новый блок для за необходимое время")
            exit(1)  # завершаем программу с ненулевым кодом выхода
    print(f"Ошибка, не нашли новый блок")
    return nonce

if __name__ == '__main__':
    difficulty_bits = 20
    check_proof_of_work('Заходи не бойся, выходи не плачь', difficulty_bits)
    check_proof_of_work('Пример блока', difficulty_bits)
    input_text = "a" * 10000000 #закинем оч большой текст
    check_proof_of_work(input_text, difficulty_bits)