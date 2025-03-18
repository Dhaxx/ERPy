import os
from . import *

class LoginScreen:
    def __init__(self, root, on_success_callback):
        self.root = root
        self.on_success_callback = on_success_callback
        self.root.title('PyERP | Login')
        
        # Imprime o diretório atual
        print("Diretório atual:", os.getcwd())
        
        # Caminho absoluto para a imagem
        img_path = os.path.join(os.path.dirname(__file__), '../static/imgs/login-img.png')
        if not os.path.exists(img_path):
            raise FileNotFoundError(f"Image not found: {img_path}")
        
        img = PhotoImage(file=img_path)

        Label(self.root, image=img, bg='#407BFF').place(x=0, y=0)
        self.img = img  # Manter uma referência para evitar que a imagem seja coletada pelo garbage collector


    # def hide(self):
    #     self.frame.pack_forget()

    def show(self):
        pass
    #     self.frame.pack(expand=True, fill='both')

    # def login(self):
    #     pass