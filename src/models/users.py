from . import Base, verify_phone_number
from sqlalchemy import Column, Integer, String, LargeBinary, DateTime, Boolean
from datetime import datetime, timezone
from email_validator import validate_email, EmailNotValidError

def current_time():
    return datetime.now(timezone.utc)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    login = Column(String(10), unique=True, nullable=False, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, index=True)
    phone = Column(String)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=current_time)
    updated_at = Column(DateTime, default=current_time, onupdate=current_time)
    is_admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    def __init__(self, **kwargs):
        # Validações antes de criar o objeto
        if 'email' in kwargs and not User.email_validation(kwargs['email']):
            raise ValueError(f'Invalid email address: {kwargs["email"]}')
        
        if 'phone' in kwargs and not verify_phone_number(kwargs['phone']):
            raise ValueError(f'Invalid phone number: {kwargs["phone"]}')
        
        # Chama o construtor da classe base (Base) após as validações
        super().__init__(**kwargs)

    @staticmethod
    def email_validation(email):
        try:
            validate_email(email)
            return True
        except EmailNotValidError as e:
            print(f"Erro ao validar email: {e}")  # Log do erro para depuração
            return False

    def __repr__(self):
        return f"<User(id={self.id}, login={self.login}, email={self.email})>"