def find_coordinates(char, square, size = 6):
    """Функция для поиска координат буквы в квадрате"""
    for row in range(size):
        for col in range(size):
            if square[row][col] == char:
                return (row, col)
    return None  # Если символ не найден

def create_alph_table(alphabet, size=6):
    """Функция формирует таблицу букв алфавита размероснтью size на size"""
    table = []
    for i in range(0, len(alphabet), size):
        row = list(alphabet[i:i+size])
        table.append(row)
    return table

def encrypt_polib(text, square):
    encrypted_text = ""
    for char in text.upper():
        coords = find_coordinates(char, square)
        if coords:
            row, col = coords
            # Заменяем букву на букву под ней (с закольцовыванием)
            new_row = (row + 1) % 6  # Если row == 5, то new_row = 0
            encrypted_text += square[new_row][col]
        else:
            encrypted_text += char  # Если символ не найден, оставляем как есть
    return encrypted_text



if __name__ == '__main__':
    from pprint import pprint
    rus_alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    pprint(create_alph_table(rus_alph))

