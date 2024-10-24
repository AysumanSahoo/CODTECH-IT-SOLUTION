class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, quantity, price):
        if name in self.items:
            print(f"Item '{name}' already exists. Updating quantity.")
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"quantity": quantity, "price": price}
        print(f"Item '{name}' added successfully.")

    def remove_item(self, name, quantity):
        if name in self.items:
            if self.items[name]["quantity"] >= quantity:
                self.items[name]["quantity"] -= quantity
                print(f"Item '{name}' removed successfully.")
            else:
                print(f"Insufficient quantity of item '{name}'.")
        else:
            print(f"Item '{name}' not found.")

    def update_price(self, name, price):
        if name in self.items:
            self.items[name]["price"] = price
            print(f"Price of item '{name}' updated successfully.")
        else:
            print(f"Item '{name}' not found.")

    def check_availability(self, name):
        if name in self.items:
            print(f"Item '{name}' is available. Quantity: {self.items[name]['quantity']}")
        else:
            print(f"Item '{name}' not found.")

    def display_inventory(self):
        print("Current Inventory:")
        for item, details in self.items.items():
            print(f"Item: {item}, Quantity: {details['quantity']}, Price: {details['price']}")

def main():
    inventory = Inventory()

    while True:
        print("\n...................Inventory Management System........................................")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Price")
        print("4. Check Availability")
        print("5. Display Inventory")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            inventory.add_item(name, quantity, price)
        elif choice == "2":
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity to remove: "))
            inventory.remove_item(name, quantity)
        elif choice == "3":
            name = input("Enter item name: ")
            price = float(input("Enter new price: "))
            inventory.update_price(name, price)
        elif choice == "4":
            name = input("Enter item name: ")
            inventory.check_availability(name)
        elif choice == "5":
            inventory.display_inventory()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
