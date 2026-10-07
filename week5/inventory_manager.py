import json
import os

INVENTORY_FILE = "inventory.json"


def load_inventory():
    if not os.path.exists(INVENTORY_FILE):
        print("inventory.json not found. Starting with an empty inventory.")
        return []

    try:
        with open(INVENTORY_FILE, "r") as f:
            data = json.load(f)
        print("inventory.json found.")
        print("Inventory loaded successfully.")
        return data
    except (json.JSONDecodeError, OSError):
        print("Warning: could not read inventory.json. Starting with an empty inventory.")
        return []


def display_all(inventory):
    print("\nCurrent Inventory")
    print("-" * 48)
    for p in inventory:
        print(f"ID: {p['id']} | Name: {p['name']} | Price: ${p['price']:.2f} | Stock: {p['stock']}")
    print("-" * 48)


def add_product(inventory, product_id, name, price, stock):
    inventory.append({
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock,
    })
    print("Product added successfully!")
    
def save_inventory(inventory):
    with open(INVENTORY_FILE, "w") as f:
        json.dump(inventory, f, indent=2)
    print("Inventory saved successfully to inventory.json.")


def find_product(inventory, product_id):
    for p in inventory:
        if p["id"].lower() == product_id.lower():
            return p
    return None


def update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ").strip()
    product = find_product(inventory, product_id)

    if product is None:
        print("Product not found.")
        return

    print("Product Found:")
    print(f"Name: {product['name']}")
    print(f"Current Stock: {product['stock']}")

    try:
        new_stock = int(input("New Stock Quantity: "))
    except ValueError:
        print("Error: stock must be a whole number.")
        return

    if new_stock < 0:
        print("Error: stock cannot be negative.")
        return

    product["stock"] = new_stock
    print("Stock updated successfully!")


def search_product(inventory):
    print("\nSearch Product")
    product_id = input("Enter Product ID: ").strip()
    product = find_product(inventory, product_id)

    if product is None:
        print("Product not found.")
        return

    print("Product Found")
    print("-" * 48)
    print(f"ID: {product['id']}")
    print(f"Name: {product['name']}")
    print(f"Price: ${product['price']:.2f}")
    print(f"Stock: {product['stock']}")
    print("-" * 48)


def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    inventory = load_inventory()

    while True:
        print("\n----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("----------------------------")

        choice = input("Enter option: ").strip()

        if choice == "1":
            display_all(inventory)

        elif choice == "2":
            print("\nAdd New Product")
            product_id = input("Product ID: ").strip()
            if find_product(inventory, product_id):
                print("Error: Product ID already exists.")
                continue
            name = input("Product Name: ").strip()
            try:
                price = float(input("Price: "))
                stock = int(input("Stock Quantity: "))
            except ValueError:
                print("Error: price must be a number and stock a whole number.")
                continue
            if price < 0 or stock < 0:
                print("Error: price and stock cannot be negative.")
                continue
            add_product(inventory, product_id, name, price, stock)

        elif choice == "3":
            update_stock(inventory)

        elif choice == "4":
            search_product(inventory)

        elif choice == "5":
            print("Saving inventory...")
            save_inventory(inventory)

        elif choice == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break

        else:
            print("Invalid option. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()