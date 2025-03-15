from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Cria e configura a conexão com meu db
engine = create_engine('sqlite:///pyERP.db', echo=False)

# Configura fábrica de sessões vinculando na minha conexão e instancia uma sessão
Session = sessionmaker(bind=engine)
session = Session()

# Cria a clase base através da fábrica de classe
Base = declarative_base()

from .users import User