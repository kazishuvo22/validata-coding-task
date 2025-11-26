from bank_account import BankAccount
from shopping_cart import ShoppingCart

def main():
    print("\n=== Testing BankAccount ===")

    acc = BankAccount("44444440001", "Kamruzzman Shuvo", 2000.0)
    acc.display_details()

    acc.deposit(3000.0)
    acc.withdraw(1500.0)
    acc.withdraw(10000.0)  # test insufficient funds
    print("Final Balance:", acc.check_balance())



    print("\n=== Testing ShoppingCart ===")

    cart = ShoppingCart()
    cart.add_item("Apple", 10, 3)
    cart.add_item("Milk", 60, 1)
    cart.add_item("Apple", 10, 2)

    cart.display_cart()

    cart.remove_item("Apple", 2)
    cart.remove_item("Milk", 1)

    cart.display_cart()
    print("Final Total Cost:", cart.total_cost())


if __name__ == "__main__":
    main()