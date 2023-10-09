# import sys

# программу не менять, только добавить два метода
# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока

class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    # здесь добавлять методы
    def insert(self, data):
        self.lst_data.append(dict(zip(self.FIELDS, data.split())))
                               
    def select(self, a, b):
        if b > len(self.lst_data):
            return self.lst_data[a:len(self.lst_data)]
        else:
            return self.lst_data[a:b+1]    


lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']
db = DataBase()
db.insert(lst_in[0])
print(db.select(0,10))