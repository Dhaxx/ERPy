from ..tests import *
from ..models.products import Product, Measure

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

@pytest.fixture
def session():
    session = Session()
    yield session
    session.close()

def test_create_measure(session):
    measure = Measure(name="Kilogram", abbreviation="kg")

    session.add(measure)
    session.commit()

    assert measure.id is not None
    assert measure.name == "Kilogram"
    assert measure.abbreviation == "kg"

def test_measure_abbreviation_default():
    measure = Measure(name="Liter")
    assert measure.abbreviation == "Lit"

def test_create_product(session):
    measure = Measure(name="Kilogram", abbreviation="kg")
    session.add(measure)
    session.commit()

    product = Product(
        name="Rice",
        description="White rice",
        measurement_id=measure.id,
        brand="Best Rice"
    )
    session.add(product)
    session.commit()

    assert product.id is not None
    assert product.name == "Rice"
    assert product.measurement_id == measure.id
    assert product.measurement == measure  # Verifica o relacionamento

def test_product_measure_relationship(session):
    measure = Measure(name="Liter", abbreviation="L")
    session.add(measure)
    session.commit()

    product = Product(
        name="Milk",
        description="Whole milk",
        measurement_id=measure.id,
        brand="Good Milk"
    )
    session.add(product)
    session.commit()

    assert product.measurement == measure
    assert measure.products == [product]  # Verifica o back-populates