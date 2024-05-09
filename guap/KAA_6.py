def str_to_list(strr):
    lst_in = strr.strip().split()
    return lst_in[:3] + lst_in[3].split('.')

def min_list(list_in):
    return min(list_in, key=lambda x: (x[0], x[1], x[2], x[3], x[4], x[5]))

def max_list(list_in):
    return max(list_in, key=lambda x: (x[0], x[1], x[2], x[3], x[4], x[5]))

def strings_to_sublits():
    """Можно объединить задания 2 и 3 в них основная часть одинакова.
    примеры проверок ввода были ранее, тут для читаемости не привожу их"""
    list_in = []
    strings_count = int(input('Укажите кол-во вводимых строк: ').strip())
    for s in range(strings_count):
        str_in =  input(f'Ввведите {s+1} строку: ')
        list_in.append(str_to_list(str_in))
    print(list_in)
    min_sublist =  min_list(list_in)
    print(min_sublist)
    print(min(min_sublist))
    max_sublist =  max_list(list_in)
    print(max_sublist)
    print(max(max_sublist))




if __name__ == '__main__':
    print(str_to_list("Белай Василий Евгеньевич 29.06.1995"))
    strings_to_sublits()
