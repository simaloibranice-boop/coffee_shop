import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer("")  # too short

    with pytest.raises(ValueError):
        Customer("A" * 20)  

def test_create_order():
    c = Customer("Alice")
    coffee = Coffee("Latte")
    order = c.create_order(coffee, 5.0)
    assert order.customer == c
    assert order.coffee == coffee
