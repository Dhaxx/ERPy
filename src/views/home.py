from . import *

class HomeScreen:
    def __init__(self, root):
        self.root = root
        self.frame = Frame(self.root)
        self.root.title('ERPy | Home')

        self.frame = Frame(width=350, height=350)
        self.frame.pack(fill='both', expand=True)
        # Configuração de responsividade
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        # Posiciona Side bar e seus componentes
        self.side_bar = SideMenu(self.frame, home_screen=self)

        self.bottom_frame = Frame(self.frame, bg='lightgray', height=20, width=300)
        self.bottom_frame.pack(side='bottom', fill='x')
        empresa_label = Label(self.bottom_frame, text='EMPRESA - ', fg=primary_color, font=('Microsoft YaHei UI Light', 10, 'bold', 'italic'), bg='lightgray')
        nome_empresa_label = Label(self.bottom_frame, text='KBTecnologia ME', font=('Microsoft YaHei UI Light', 11, 'italic'), bg='lightgray')
        nome_empresa_label.pack(side='right', padx=(0,20))
        empresa_label.pack(side='right')
        
        # Posiciona Frame de conteúdo
        self.content = Frame(self.frame)
        self.content.pack(fill='both', expand=True)

    def show(self):
        self.root.deiconify()

    def showTransactionScreen(self):
        for widget in self.content.winfo_children():
            widget.destroy()
        self.root.title('ERPy | Movimentação')
        transaction_frame = TransactionScreen(self.content)
        self.content = transaction_frame

class SideMenu(Frame):
    def __init__(self, master, home_screen):
        super().__init__(master, width=250, bg='white')
        self.home_screen = home_screen
        self.pack(side='left', fill='y')

        Frame(self, height=20, bg='white').pack(side='top')
        Label(self, text='ERPy', padx=50, fg=primary_color, bg="white",
              font=('Microsoft YaHei UI Light', 23, 'bold')).pack(side='top')
        Label(self, text='Gestão Inteligente para o Seu Negócio', fg='black',
              bg='white', font=('Microsoft YaHei UI Light', 6)).pack(side='top')
        Frame(self, height=20, bg='white').pack(side='top')

        SideMenuButtons(self, text='Movimentação', action=home_screen.showTransactionScreen)
        SideMenuButtons(self, text='Balanço')

class SideMenuButtons(Button):
    def __init__(self, master, **kwargs):
        self.command = kwargs['action'] if 'action' in kwargs else None
        super().__init__(master, text=kwargs['text'], padx=8, pady=5, border=0, width=20, bg=primary_color, fg='white', cursor='hand2',command=self.command)
        self.pack(side='top', pady=10)

class TransactionScreen(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(fill='both', expand=True)

        self.actions_hud = ActionHud(self)
        # self.insert_btn = Button(self, text='Inserir')
        # self.insert_btn.pack(side='top')

class ActionHud(Frame):
    def __init__(self, master):
        Frame(master, height=70).pack(side='top')
        super().__init__(master, height=80, pady=30, bg='green')
        self.master = master
        self.pack(side='top', fill='x')

        self.insert_btn = ActionButton(self, text='Inserir')

class ActionButton(Button):
    def __init__(self, master, **kwargs):
        self.command = kwargs['action'] if 'action' in kwargs else None
        super().__init__(master, text=kwargs['text'], padx=10, width=10, cursor='hand2', command=self.command)
        self.pack(side='left', padx=(20,0))