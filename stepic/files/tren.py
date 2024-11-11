import os
import chardet # type: ignore
# source step_env/bin/activate

def search_tren(num_tren_in):
    with open("train.txt", 'rb') as file_enc:
        #определяем их кодировку, ибо я пока хз как ее иначе понять
        result = chardet.detect(file_enc.read())
        encoding_in = result['encoding']

    with open("train.txt", 'r', encoding=encoding_in) as file_out:
        list_tren = file_out.read().split('\n')
        for tren in list_tren:
            if num_tren_in == tren.split()[1].replace(',',''):
                print(*tren.split()[2:])


if __name__ == '__main__':
    num_tren = input('Номер тренировки: ').strip()
    if 0 <=int(num_tren)<= 13:
        search_tren(num_tren)
    else:
        print('No info')
