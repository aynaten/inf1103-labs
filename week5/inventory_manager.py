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


def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    inventory = load_inventory()
    display_all(inventory)


if __name__ == "__main__":
    main()