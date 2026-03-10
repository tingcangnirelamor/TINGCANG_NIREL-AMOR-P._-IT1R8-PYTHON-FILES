class ItemInfo:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Shopping_Cart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        item = ItemInfo(name, price)  
        self.items.append(item)
        print(f"{name} has been added to your cart.")

    def remove_item(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                self.items.remove(item)
                print(f"{name} has been removed from your cart.")
                return
        print("Item is not found in cart.")

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
            return

        print("\nItems in your cart:")
        total = 0
        for item in self.items:
            print(f"{item.name} - ${item.price}")
            total += item.price
        print(f"Total Amount: ${total}")

    def checkout(self):
        total = sum(item.price for item in self.items)
        print(f"Total amount to pay: ${total}")
        print("Thank you for shopping, come again!")
        self.items.clear()

def main():
    cart = Shopping_Cart()   

    while True:
        print("\n=== Menu ===")
        print("1. Add an Item")
        print("2. Remove an Item")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Choose an option from the menu: ")

        if choice == "1":
            name = input("Enter the item name: ")
            price = float(input("Enter the item price: "))
            cart.add_item(name, price)

        elif choice == "2":
            name = input("Enter the item name you want to remove: ")
            cart.remove_item(name)

        elif choice == "3":
            cart.view_cart()

        elif choice == "4":
            cart.checkout()

        elif choice == "5":
            print("Exit.")
            break

        else:
            print("Please pick from 1 to 5.")

main()