from . import *

class HomeScreen:
    def __init__(self, root):
        self.root = root
        self.frame = Frame(self.root)
        self.root.title('ERPy | Home')

        self.frame = Frame(width=350, height=350, bg='white')
        self.frame.pack(fill='both', expand=True)
        # Configuração de responsividade
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        self.root.bind('<Configure>', self.on_resize)

    def on_resize(self, e):
        width = self.root.winfo_width()
        height = self.root.winfo_height()

        self.heading.grid(padx=width//2 - 100, pady=height//2 - 50)

    def show(self):
        self.root.deiconify()