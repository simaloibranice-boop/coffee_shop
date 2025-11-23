import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_price_validation():
    c = Customer("Test")
    coffee = Coffee("Strong")
    
    with pytest.raises(ValueError):
        Order(c, coffee, 0.5)  

    with pytest.raises(ValueError):
        Order(c, coffee, 20)  
