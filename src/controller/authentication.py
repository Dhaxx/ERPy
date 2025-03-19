from ..models.users import User
from ..models import session  # Usar a sessão já existente
from hashlib import sha256

class AuthController:
    def __init__(self, view, on_success_callback):
        self.view = view
        self.on_success_callback = on_success_callback

    def login(self, username, password):
        if not username or not password:
            self.view.show_error("Por favor, preencha todos os campos.")
            return

        user = session.query(User).filter(User.login == username).first()
        try:
            if user:
                password_hash = sha256(password.encode()).hexdigest()
                print(password_hash)
                if user.password_hash == password_hash:
                    self.on_success_callback()  # Autenticação bem-sucedida
        except Exception as e:
            print(e)
            self.view.show_error("Usuário ou senha incorretos.")