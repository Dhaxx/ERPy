from . import *

class HomeScreen:
    def __init__(self, root):
        self.root = root
        self.frame = Frame(self.root)
        self.root.title('ERPy | Home')

        self.label = Label(self.frame, text='Bem-vindo ao PyERP')
        self.label.pack()
    
    def show(self):
        self.frame.pack()