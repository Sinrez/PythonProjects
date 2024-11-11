import os
import chardet # type: ignore

def search(word):
    res = []
    for root, dirs, files in os.walk("./"):
        #обходим каталоги
        for file in files:
            #ищем текстовые файлы по их расширению
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as file_enc:
                    #определяем их кодировку, ибо я пока хз как ее иначе понять
                    result = chardet.detect(file_enc.read())
                    encoding_in = result['encoding']
                with open(file_path, 'r', encoding=encoding_in) as file_out:
                    if word.lower() in file_out.read().lower():
                        #ищем наше слово в файле и если нашли, то запоминаем имя файла
                        res.append(file)
    return res

if __name__ == '__main__':
    inp_word = input('Введите слово: ').strip()
    print('\n'.join(search(inp_word)))
