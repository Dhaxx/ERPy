from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import re

# Cria e configura a conexão com meu db
engine = create_engine('sqlite:///pyERP.db', echo=False)

# Configura fábrica de sessões vinculando na minha conexão e instancia uma sessão
Session = sessionmaker(bind=engine)
session = Session()

# Cria a clase base através da fábrica de classe
Base = declarative_base()

# Validador de número de celular
def verify_phone_number(number):
    model = re.compile(r'^(?:\+55)?\s?(?:\(?\d{2}\)?)?\s?(?:9?\d{4}[-\.\s]?\d{4})$')

    if model.match(number):
        return True
    else:
        return False

from .users import User
from .products import Measure, Product
from .clients import Client

Base.metadata.create_all(engine)

def create_default_user():
    from hashlib import sha256
    # Dados do novo usuário
    username = "recrutador"
    password = "abc123"
    password_hash = sha256(password.encode()).hexdigest()  # Gera hash da senha

    # Cria usuário padrão
    new_user = User(
        login=username,
        password_hash=password_hash,
        first_name="Fulano",
        last_name="Silva",
        email='fulanoSilva@gmail.com'
    )

    # Adicionando ao banco e salvando
    try:
        session.add(new_user)
        session.commit()
        print("Usuário inserido com sucesso!")
    except Exception as e:
        e
        session.rollback()
        pass