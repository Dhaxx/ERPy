from . import *

class LoginScreen:
    def __init__(self, root, on_success_callback):
        self.root = root
        self.on_success_callback = on_success_callback
        self.root.title('ERPy | Login')
                
        # Caminho absoluto para a imagem
        img_path = find_picture('../static/imgs/login-img.png')
        img = PhotoImage(file=img_path)

        Label(self.root, image=img, bg=PRIMARY_COLOR).place(x=0, y=0)
        self.img = img  # Manter uma referência para evitar que a imagem seja coletada pelo garbage collector

        self.Frame = Frame(width=350,height=350,bg='white')
        self.Frame.place(x=540, y=70)

        heading = Label(self.Frame,text='ERPy',fg=PRIMARY_COLOR,bg="white",font=('Microsoft YaHei UI Light',23,'bold'))
        heading.place(x=130,y=30)
        subheading=Label(self.Frame,text='Gestão Inteligente para o Seu Negócio',fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
        subheading.place(x=65,y=75)

        username = Entry(self.Frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
        username.place(x=70,y=140)
        username.insert(0,'User')

        username_icon_path = find_picture('../static/icons/person_blue.png')
        username_icon = PhotoImage(file=username_icon_path)
        self.username_icon = username_icon

        Label(self.Frame,image=username_icon,bg="white",width=23,height=23).place(x=42,y=138)
        Frame(self.Frame,width=204,height=2,bg='black').place(x=69,y=163)

        password = Entry(self.Frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11), show='*')
        password.place(x=70,y=200)
        password.insert(0, '')

        password_icon_path = find_picture('../static/icons/lock_blue.png')
        password_icon = PhotoImage(file=password_icon_path)
        self.password_icon = password_icon

        Label(self.Frame,image=password_icon,bg="white",width=23,height=23).place(x=42,y=197)
        Frame(self.Frame,width=204,height=2,bg='black').place(x=69,y=223)

        Button(self.Frame,width=39,pady=7,text='Login',bg=PRIMARY_COLOR,fg='white',border=0,cursor='hand2').place(x=35,y=274)
        label=Label(self.Frame,text='Não possui acesso?',fg='black',bg='white',font=('Microsoft YaHei UI Light',7))
        label.place(x=90,y=310)

        btn_recrutador = Button(self.Frame,width=20,text='Entrar como recrutador',border=0,fg=PRIMARY_COLOR,bg='white',font=(('Microsoft YaHei UI Light',7)), cursor='hand2')
        btn_recrutador.place(x=175,y=310)

    # def hide(self):
    #     self.frame.pack_forget()

    def show(self):
        pass
    #     self.frame.pack(expand=True, fill='both')

    # def login(self):
    #     pass