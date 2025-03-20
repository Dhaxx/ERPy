from . import *
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(Text)
    measurement_id = Column(Integer, ForeignKey('measures.id'), nullable=False)
    brand = Column(String)
    measurement = relationship('Measure', back_populates='products')

    def __repr__(self):
        return f'<Product(id={self.id} - name={self.name} - mesurement_id ={self.measurement_id})>'

class Measure(Base):
    __tablename__ = 'measures'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    abbreviation = Column(String) 
    products = relationship('Product', back_populates='measurement')

    def __repr__(self):
        return f'<Measure(id={self.id} - name={self.name} - abbreviation={self.abbreviation})>'
    
    def __init__(self, **kwargs):
        if 'abbreviation' not in kwargs:
            self.abbreviation = kwargs['name'][:3]
        super().__init__(**kwargs)