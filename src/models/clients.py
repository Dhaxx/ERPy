from . import Base, verify_phone_number
from sqlalchemy import Column, Integer, String

class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    cep = Column(String)
    street = Column(String)
    number = Column(String)
    city = Column(String)

    def __repr__(self):
        return f'<Client(id={self.id} - name={self.first_name} {self.last_name} - phone={self.phone})>'
    
    def __init__(self, **kwargs):
        if 'phone' in kwargs and not verify_phone_number(kwargs['phone']):
            raise ValueError(f'Invalid phone number: {kwargs["phone"]}')
        super().__init__(**kwargs)