class CashRegister:

    def __init__(self, discount=0):
        # It sets the discount
        self.discount = discount

        # The total starts at 0
        self.total = 0

        # Items starts as an empty list
        self.items = []

        # Previous transactions starts as an empty list
        self.previous_transactions = []

    # Discount property
    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        # Discount must be an integer between 0 and 100
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0

    # It adds an item to the register
    def add_item(self, item, price, quantity=1):
        # Add the price to the total
        self.total += price * quantity

        # Add the item for each quantity
        for i in range(quantity):
            self.items.append(item)

        # Save the transaction
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    # Apply discount
    def apply_discount(self):
        # If there is no discount
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        # Calculate the discount
        discount_amount = self.total * (self.discount / 100)

        # Subtract the discount from total
        self.total -= discount_amount

        # Print the updated total
        print(f"After the discount, the total comes to ${int(self.total)}.")

    # Void the last transaction
    def void_last_transaction(self):
        # Check if there are no transactions
        if not self.previous_transactions:
            return

        # Get the last transaction
        transaction = self.previous_transactions.pop()

        # Get the price and quantity
        price = transaction["price"]
        quantity = transaction["quantity"]

        # Remove the transaction price from total
        self.total -= price * quantity

        # Remove all items from the last transaction
        for i in range(quantity):
            self.items.pop()