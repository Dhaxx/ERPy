from ..tests import *
from ..models.clients import Client

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def test_create_client_with_valid_phone():
    client = Client(
        first_name = "fulano",
        last_name = "da silva",
        phone = "11987654321"
    )
    session.add(client)
    session.commit()
    assert client.id is not None

def test_create_client_with_invalid_phone():
    with pytest.raises(ValueError) as excinfo:
        client = Client(
            first_name = "fulano",
            last_name = "da silva",
            phone = "12345-6789"
        )
    assert "Invalid phone number: "in str(excinfo.value)

def test_repr():
    client = Client(
        first_name = "fulano",
        last_name = "da silva",
        phone = "11987654321"
    )
    assert repr(client) == '<Client(id=None - name=fulano da silva - phone=11987654321)>'