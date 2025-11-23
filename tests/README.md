
# Coffee Shop OOP Project

## Overview
This project models a Coffee Shop using Python OOP.  
It has three main classes: `Customer`, `Coffee`, and `Order`, with these relationships:  

- A Customer can place many Orders  
- A Coffee can have many Orders  
- An Order belongs to one Customer and one Coffee  

---

## Project Structure
```

coffee_shop/
  - customer.py
 - coffee.py
 - order.py
  - debug.py
 - tests/
  - Pipfile
 - README.md

````

---

## Features
- **Customer**: create orders, view orders and coffees, most aficionado per coffee  
- **Coffee**: list orders/customers, count orders, average price  
- **Order**: links a customer and coffee with validated price  

---

## Setup
```bash
git clone https://github.com/simaloibranice-boop/coffee_shop.git
cd coffee_shop
pipenv install
pipenv shell
pipenv install pytest
pytest
```

## Author

Branice Nashilu – Moringa School Student

