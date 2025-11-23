import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from coffee import Coffee
from customer import Customer

def test_coffee_name_validation():
    import pytest
    with pytest.raises(ValueError):
        Coffee("A")

def test_num_orders_and_average():
    c1 = Customer("Branice")
    c2 = Customer("Bob")
    latte = Coffee("Latte")

    c1.create_order(latte, 4.0)
    c2.create_order(latte, 6.0)

    assert latte.num_orders() == 2
    assert latte.average_price() == 5.0
