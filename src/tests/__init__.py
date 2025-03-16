import pytest
from ..models import Base, sessionmaker, create_engine

# Configuração do banco de dados em memória para testes
engine = create_engine('sqlite:///:memory:')