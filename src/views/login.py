from . import *
from ..controller.authentication import AuthController

class LoginScreen:
    def __init__(self, root, on_success_callback):
        self.root = root
        self.on_success_callback = on_success_callback
        self.root.title('ERPy | Login')
        self.controller = AuthController(self, self.on_success_callback)
                
        img_path = find_picture('../static/imgs/login-img.png')
        img = PhotoImage(file=img_path)

        self.background_img = Label(self.root, image=img, bg=primary_color)
        self.background_img.place(x=0, y=0)
        self.img = img  # Manter uma referência para evitar que a imagem seja coletada pelo garbage collector

        self.frame = LoginForm(self.root, login_screen=self)
        self.frame.place(x=540, y=70)
    
    def show_error(self, message):
        messagebox.showerror('Erro', message)

    def hide(self):
        self.background_img.destroy()
        self.frame.destroy()
        self.img.blank()
        self.root.withdraw()

    def on_login(self):
        username = self.frame.username.get()
        password = self.frame.password.get()

        self.controller.login(username, password)

class LoginForm(Frame):
    def __init__(self, master, login_screen):
        super().__init__(master, width=350, height=350, bg='white')

        heading = Label(self, text='ERPy', fg=primary_color, bg="white", font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=130, y=30)
        subheading = Label(self, text='Gestão Inteligente para o Seu Negócio', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
        subheading.place(x=65, y=75)

        # Implementa campo de entrada de usuário
        self.username = Entry(self, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
        self.username.place(x=70, y=140)
        self.username.insert(0, 'User')
        self.username.bind('<FocusIn>', self.on_enter)
        self.username.bind('<FocusOut>', self.on_leave)
        self.username.bind('<KeyRelease>', self.username_validate)

        username_icon_path = find_picture('../static/icons/person_blue.png')
        username_icon = PhotoImage(file=username_icon_path)
        self.username_icon = username_icon

        Label(self, image=username_icon, bg="white", width=23, height=23).place(x=42, y=138)
        Frame(self, width=204, height=2, bg='black').place(x=69, y=163)

        # Implementa campo de entrada para senha
        self.password = Entry(self, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11), show='*')
        self.password.place(x=70, y=200)
        self.password.insert(0, 'Password')
        self.password.bind('<FocusIn>', self.on_enter_password)
        self.password.bind('<FocusOut>', self.on_leave_password)

        password_icon_path = find_picture('../static/icons/lock_blue.png')
        password_icon = PhotoImage(file=password_icon_path)
        self.password_icon = password_icon

        Label(self, image=password_icon, bg="white", width=23, height=23).place(x=42, y=197)
        Frame(self, width=204, height=2, bg='black').place(x=69, y=223)

        # Botão de visualização de senha
        self.visibility_icon_path_visible = find_picture('../static/icons/visible.png')
        self.visibility_icon_path_invisible = find_picture('../static/icons/invisible.png')
        self.visibility_icon = PhotoImage(file=self.visibility_icon_path_visible)
        self.visibility_password_btn = Button(
            self, width=28, image=self.visibility_icon, bg='white', border=0, cursor='hand2', command=self.toggle_password_visibility
        )
        self.visibility_password_btn.place(x=260, y=200)
        self.password_visible = False

        Button(self, width=39, pady=7, text='Login', bg=primary_color, fg='white', border=0, cursor='hand2', command=login_screen.on_login).place(x=35, y=274)
        label = Label(self, text='Não possui acesso?', fg='black', bg='white', font=('Microsoft YaHei UI Light', 7))
        label.place(x=90, y=310)

        btn_recrutador = Button(self, width=20, text='Entrar como recrutador', border=0, fg=primary_color, bg='white', font=(('Microsoft YaHei UI Light', 7)), cursor='hand2', command=self.guest_login)
        btn_recrutador.place(x=175, y=310)

    def on_enter(self, e):
        if self.username.get() == 'User':
            self.username.delete(0, 'end')

    def on_leave(self, e):
        name = self.username.get()
        if name == '':
            self.username.insert(0, 'User')

    def on_enter_password(self, e):
        if self.password.get() == 'Password':
            self.password.delete(0, 'end')

    def on_leave_password(self, e):
        password = self.password.get()
        if password == '':
            self.password.insert(0, 'Password')

    def toggle_password_visibility(self):
        if self.password_visible:
            self.password.configure(show='*')
            self.visibility_icon = PhotoImage(file=self.visibility_icon_path_visible)
            self.password_visible = False
        else:
            self.password.configure(show='')
            self.visibility_icon = PhotoImage(file=self.visibility_icon_path_invisible)
            self.password_visible = True
        
        self.visibility_password_btn.config(image=self.visibility_icon)
        self.visibility_password_btn.image = self.visibility_icon  # Manter uma referência ao ícone

    def username_validate(self, e):
        current_text = self.username.get()
        lower_text = current_text.lower()
        validated_text = ''.join([char for char in lower_text if char.islower() or char == '_'])
        
        if current_text != validated_text:
            self.username.delete(0, 'end')
            self.username.insert(0, validated_text)

    def guest_login(self):
        self.username.delete(0, 'end')
        self.username.insert(0,'recrutador')
        self.password.delete(0, 'end')
        self.password.insert(0,'abc123')