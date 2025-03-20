from tkinter import *
from tkinter import messagebox
import os

primary_color = '#57a1f8'

# Janela principal
class MainWindow(): 
    def __init__(self):
        self.root = Tk()
        self.root.title('PyERP')
        self.root.geometry('925x500+300+200')
        self.root.configure(bg='#fff')
        self.root.resizable(False,False)
        self.login_screen = LoginScreen(self.root, self.show_main_window)

    def show_main_window(self):
        self.login_screen.hide() # Esconde a tela de login
        from .home import HomeScreen
        self.root.resizable(True,True)
        self.main_window = HomeScreen(self.root)
        self.main_window.show()

    def run(self):
        self.root.mainloop()
    
def find_picture(path):
    absolute_path = os.path.join(os.path.dirname(__file__), f'{path}')
    if not os.path.exists(absolute_path):
            raise FileNotFoundError(f"Image not found: {absolute_path}")
    return absolute_path
    
from .login import LoginScreen