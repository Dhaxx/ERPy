from . import *

class LoginScreen:
    def __init__(self, root, on_success_callback):
        self.root = root
        self.on_success_callback = on_success_callback
        self.root.title('PyERP | Login')
                
        # Caminho absoluto para a imagem
        img_path = find_picture('../static/imgs/login-img.png')
        img = PhotoImage(file=img_path)

        Label(self.root, image=img, bg='#407BFF').place(x=0, y=0)
        self.img = img  # Manter uma referência para evitar que a imagem seja coletada pelo garbage collector

        self.Frame = Frame(width=350,height=350,bg='white')
        self.Frame.place(x=540, y=70)

        heading = Label(self.Frame,text='Login',fg='#57a1f8',bg="white",font=('Microsoft YaHei UI Light',23,'bold'))
        heading.place(x=130,y=20)

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

        

    # def hide(self):
    #     self.frame.pack_forget()

    def show(self):
        pass
    #     self.frame.pack(expand=True, fill='both')

    # def login(self):
    #     pass