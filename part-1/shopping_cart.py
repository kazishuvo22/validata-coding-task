class ShoppingCart:
    def __init__(self):
        '''
        Item Input Example:
            {
                "item_name": { "price": x, "qty": y}
            }
        '''
        self.items = {}

    def add_item(self, name:str, price:float, quantity:int=1):
        if name in self.items:
            self.items[name]["qty"] += quantity
        else:
            self.items[name] = {"price": price, "qty": quantity}
        print(f"Added {quantity} x {name} to cart.")

    def remove_item(self, name:str, quantity=1):
        if name not in self.items:
            print("Item not found in cart.")
            return

        if quantity >= self.items[name]["qty"]:
            del self.items[name]
            print(f"Removed {name} from cart.")
        else:
            self.items[name]["qty"] -= quantity
            print(f"Removed {quantity} x {name}.")

    def total_cost(self):
        return sum(
            info["price"] * info["qty"]
            for info in self.items.values()
        )

    def display_cart(self):
        print("----- Shopping Cart -----")
        if not self.items:
            print("Cart is empty.")
            return

        for item, info in self.items.items():
            print(f"{item} - Qty: {info['qty']} | Price: {info['price']}")
        print(f"Total Cost: {self.total_cost()}")