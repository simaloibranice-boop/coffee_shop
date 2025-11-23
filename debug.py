from customer import Customer
from coffee import Coffee
from order import Order


alice = Customer("Alice")
bob = Customer("Bob")
carol = Customer("Carol")

latte = Coffee("Latte")
espresso = Coffee("Espresso")
cappuccino = Coffee("Cappuccino")


alice.create_order(latte, 3.5)
alice.create_order(espresso, 4.0)
bob.create_order(latte, 3.0)
bob.create_order(cappuccino, 5.0)
carol.create_order(espresso, 4.5)
carol.create_order(latte, 3.2)

print("Alice's orders:", [order.coffee.name for order in alice.orders()])
print("Alice's coffees:", [coffee.name for coffee in alice.coffees()])

print("Bob's orders:", [order.coffee.name for order in bob.orders()])
print("Bob's coffees:", [coffee.name for coffee in bob.coffees()])


print("Latte orders:", [order.customer.name for order in latte.orders()])
print("Latte customers:", [customer.name for customer in latte.customers()])
print("Most aficionado for Latte:", Customer.most_aficionado(latte).name)
print("Latte total orders:", latte.num_orders())
print("Latte average price:", latte.average_price())

print("Espresso orders:", [order.customer.name for order in espresso.orders()])
print("Espresso customers:", [customer.name for customer in espresso.customers()])
print("Espresso total orders:", espresso.num_orders())
print("Espresso average price:", espresso.average_price())

print("Cappuccino orders:", [order.customer.name for order in cappuccino.orders()])
print("Cappuccino customers:", [customer.name for customer in cappuccino.customers()])
print("Cappuccino total orders:", cappuccino.num_orders())
print("Cappuccino average price:", cappuccino.average_price())
