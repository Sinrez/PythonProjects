from tkinter import *
class Block:
    def __init__(self, master, func):
        self.ent = Entry(master, width=20)
        self.but = Button(master,
                        text="Преобразовать")
        self.lab = Label(master, width=20,
                        bg='black', fg='white')
        self.but['command'] = eval('self.' + func)
        self.ent.pack()
        self.but.pack()
        self.lab.pack()
    def str_to_sort(self):
        s = self.ent.get()
        s = s.split()
        s.sort()
        self.lab['text'] = ' '.join(s)
    def str_reverse(self):
        s = self.ent.get()
        s = s.split()
        s.reverse()
        self.lab['text'] = ' '.join(s)
root = Tk()
first_block = Block(root, 'str_to_sort')
second_block = Block(root, 'str_reverse')
root.mainloop()