def read_from_file():
    try:
        res=[]
        with open('prices.txt', 'r', encoding='koi8-r') as file:
            for f in file:
                a, b, c = f.strip().split('\t')
                res.append(int(b) * int(c))
            print(sum(res))
    except FileNotFoundError:
        print("Файл не найден.")
    except LookupError:
        print("Неправильная кодировка.")
    except UnicodeDecodeError:
        print("Ошибка декодирования файла. Проверьте кодировку.")

if __name__ == '__main__':
    read_from_file()