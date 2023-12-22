class WindowDlg:
    def __init__(self, title, width, height) -> None:
        self.__title = title
        self.__width = self.__height = None
        self.width = width
        self.height = height
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if type(value) == int and 0 <= value <= 10000:
            if self.__width:
                self.show()
            self.__width = value
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if type(value) == int and 0 <= value <= 10000:
            if self.__height:
                self.show()
            self.__height = value    

    def show(self):
        return f"{self.__title}: {self.__width}, {self.__height}"


wnd = WindowDlg("Диалог 1", 100, 50)
print(wnd.show())