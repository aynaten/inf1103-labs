
import json
import os

from physical_product import PhysicalProduct
from digital_product import DigitalProduct


# ============================================================
# FILE HANDLING
# ============================================================

def save_inventory(inventory):
    products_data = []

    # Convert each product into a dictionary
    for product in inventory.get_products():
        products_data.append(product.to_dict())

    # Save product data into JSON
    with open("inventory.json", "w") as file:
        json.dump(products_data, file, indent=4)

    print("Inventory saved successfully.")


def load_inventory(inventory):
    # Check whether the file exists
    if not os.path.exists("inventory.json"):
        return

    try:
        with open("inventory.json", "r") as file:
            products_data = json.load(file)

        if not isinstance(products_data, list):
            print("Invalid inventory file format.")
            return

        # Restore each saved product based on its type
        for data in products_data:
            try:
                product_type = data.get("type")

                if product_type == "physical":
                    product = PhysicalProduct(
                        data["id"],
                        data["name"],
                        data["price"],
                        data["stock"],
                        data["weight"]
                    )

                elif product_type == "digital":
                    product = DigitalProduct(
                        data["id"],
                        data["name"],
                        data["price"],
                        data["stock"],
                        data["download_size"]
                    )

                else:
                    print("Unknown product type. Skipping product.")
                    continue

                inventory.add_product(product)

            except (KeyError, TypeError, ValueError, AttributeError):
                print("Invalid product data. Skipping product.")

        print("Inventory loaded successfully.")

    except (OSError, json.JSONDecodeError):
        print("Unable to load inventory.json.")
