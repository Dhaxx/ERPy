from . import *
from src.models.users import User

# Configuração do banco de dados em memória para testes
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def test_create_user_with_valid_email():
    user = User(
        login="joao123",
        password_hash=b"hash_da_senha",
        first_name="João",
        last_name="Silva",
        email="joao@gmail.com",
        phone="987654321"
    )
    session.add(user)
    session.commit()
    assert user.id is not None

def test_create_user_with_invalid_email():
    with pytest.raises(ValueError) as excinfo:
        user = User(
            login="maria123",
            password_hash=b"hash_da_senha",
            first_name="Maria",
            last_name="Santos",
            email="invalid-email",
            phone="987654321"
        )
    assert "Invalid email address" in str(excinfo.value)

def test_email_validation():
    user = User(
        login="testuser",
        password_hash=b"hash_da_senha",
        first_name="Test",
        last_name="User",
        email="test@hotmail.com",
        phone="987654321"
    )
    assert user.email_validation(user.email) == True

    user.email = "invalid-email"
    assert user.email_validation(user.email) == False

def test_repr():
    user = User(
        login="testuser",
        password_hash=b"hash_da_senha",
        first_name="Test",
        last_name="User",
        email="test@gmail.com",
        phone="987654321"
    )
    assert repr(user) == "<User(id=None, login=testuser, email=test@gmail.com)>"

def test_create_user_with_invalid_phone_number():
    with pytest.raises(ValueError) as excinfo:
        user = User(
        login="joao123",
        password_hash=b"hash_da_senha",
        first_name="João",
        last_name="Silva",
        email="joao@gmail.com",
        phone="12345-6789"
    )
    assert "Invalid phone number: "in str(excinfo.value)