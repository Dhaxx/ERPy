from . import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(Text)
    measurement_id = Column(Integer, ForeignKey('measure.id'), nullable=False)
    brand = Column(String)
    measurement = relationship('Measure', back_populates='products')

class Measure(Base):
    __tablename__ = 'measures'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    abbreviation = Column(String, nullable=False, default=lambda context: context.current_parameters['name'][:3])
    products = relationship('Product', back_populates='measurement')