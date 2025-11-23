class Customer:
    all_customers = []

    def __init__(self, name: str):
        """
        Initialize a Customer with a validated name.
        """
        self.name = name
        Customer.all_customers.append(self)

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters.")
        self._name = value 

    def orders(self):
        from order import Order
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
       from order import Order
       return list({order.coffee for order in self.orders()})

    
    def create_order(self, coffee, price):
        from order import Order 
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order

        coffee_orders = [order for order in Order.all_orders if order.coffee == coffee]

        if not coffee_orders:
            return None

        spending = {}

        for order in coffee_orders:
            spending[order.customer] = spending.get(order.customer, 0) + order.price

        return max(spending, key=spending.get)
