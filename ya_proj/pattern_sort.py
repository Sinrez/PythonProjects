import sys


def sort_with_template(n, arr, m, template):
    # Создание словаря для хранения количества встречающихся элементов
    count_dict = {}
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    result = []
    
    # Проход по шаблону
    for num in template:
        if num in count_dict:
            result.extend([num] * count_dict[num])
            del count_dict[num]
    
    # Добавление оставшихся элементов, отсортированных по возрастанию
    for num, count in sorted(count_dict.items()):
        result.extend([num] * count)
    
    return result


if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    arr = sys.stdin.readline().rstrip().split()
    m = int(sys.stdin.readline().rstrip())
    template = sys.stdin.readline().rstrip().split()
    result = sort_with_template(n, arr, m, template)
    print(' '.join(map(str, result)))   