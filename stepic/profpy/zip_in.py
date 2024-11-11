from zipfile import ZipFile

# with ZipFile('test.zip') as zip_file:
#     zip_file.printdir()

# with ZipFile('test.zip') as zip_file:
#     info = zip_file.infolist()
#     print(info[6].file_size)                # размер начального файла в байтах
#     print(info[6].compress_size)            # размер сжатого файла в байтах
#     print(info[6].filename)                 # имя файла
#     print(info[6].date_time)                # дата изменения файла

# with ZipFile('test.zip') as zip_file:
#     info = zip_file.namelist()
#     print(*info, sep='\n')

# with ZipFile('test.zip') as zip_file:
#     with zip_file.open('test/Разные файлы/astros.json') as file:
#         print(file.read())

# with ZipFile('test.zip') as zip_file:
#     with zip_file.open('test/Разные файлы/astros.json') as file:
#         print(file.read().decode('utf-8'))

with ZipFile('archive.zip', mode='w') as zip_file:
    zip_file.write('countr.py')
    zip_file.write('data1.json')
    print(zip_file.namelist())

