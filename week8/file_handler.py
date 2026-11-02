
import json
import os

from product import Product


# ============================================================
# FILE HANDLING
# ============================================================

def save_inventory(inventory):
    # Create an empty list to store product dictionaries
    products_data = []

    # Convert each Product object into a dictionary
    for product in inventory.get_products():
        products_data.append(product.to_dict())

    # Open inventory.json in write mode and save the data
    with open("inventory.json", "w") as file:
        json.dump(products_data, file, indent=4)

    print("Inventory saved successfully.")


def load_inventory(inventory):
    # Check if the inventory file exists
    if not os.path.exists("inventory.json"):
        return

    # Open inventory.json and load the saved dictionaries
    with open("inventory.json", "r") as file:
        products_data = json.load(file)

    # Convert each dictionary back into a Product object
    for data in products_data:
        product = Product(
            data["id"],
            data["name"],
            data["price"],
            data["stock"]
        )

        # Add the restored product to Inventory
        inventory.add_product(product)

    print("Inventory loaded successfully.")
