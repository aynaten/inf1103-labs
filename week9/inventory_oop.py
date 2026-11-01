
import json
import os
import math
from abc import ABC, abstractmethod


# ============================================================
# PRODUCT CLASS (ABSTRACT)
# ============================================================

class Product(ABC):
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self):
        return self.__product_id

    def to_dict(self):
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }

    def update_stock(self, quantity):
        if quantity >= 0:
            self.__stock = quantity
            print("Stock updated successfully.")
        else:
            print("Stock cannot be negative.")

    def display_information(self):
        print(f"Product ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")

    @abstractmethod
    def get_fulfilment_info(self):
        pass


# ============================================================
# CAN BE SHIPPED INTERFACE
# ============================================================

class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass


# ============================================================
# PHYSICAL PRODUCT CLASS
# ============================================================

class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    def display_information(self):
        super().display_information()
        print("Product Type: Physical")
        print(f"Weight: {self.__weight} kg")

    def get_fulfilment_info(self):
        return "This product requires physical shipping."

    def calculate_shipping_cost(self):
        shipping_rate = 5.00
        return self.__weight * shipping_rate

    # Extend the parent's dictionary with physical product details
    def to_dict(self):
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data


# ============================================================
# DIGITAL PRODUCT CLASS
# ============================================================

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def display_information(self):
        super().display_information()
        print("Product Type: Digital")
        print(f"Download Size: {self.__download_size} MB")

    def get_fulfilment_info(self):
        return "This product is delivered digitally."

    # Extend the parent's dictionary with digital product details
    def to_dict(self):
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self.__download_size
        return data


# ============================================================
# INTERFACE REGISTRATION
# ============================================================

CanBeShipped.register(PhysicalProduct)


# ============================================================
# INVENTORY CLASS
# ============================================================

class Inventory:
    def __init__(self):
        self.__products = []

    def get_products(self):
        return self.__products

    def add_product(self, product):
        if self.search_product(product.get_product_id()) is not None:
            print("Product ID already exists.")
            return

        self.__products.append(product)
        print("Product added successfully.")

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def display_all(self):
        if not self.__products:
            print("Inventory is empty.")
            return

        for product in self.__products:
            print("--------------------")
            product.display_information()
            print(product.get_fulfilment_info())

            if isinstance(product, CanBeShipped):
                print(f"Shipping Cost: ${product.calculate_shipping_cost():.2f}")


# ============================================================
# FILE HANDLING
# ============================================================

def save_inventory(inventory):
    products_data = []

    # Convert each product object into a dictionary
    for product in inventory.get_products():
        products_data.append(product.to_dict())

    # Write all product dictionaries to the JSON file
    with open("inventory.json", "w") as file:
        json.dump(products_data, file, indent=4)

    print("Inventory saved successfully.")


def load_inventory(inventory):
    # Start with an empty inventory if no saved file exists
    if not os.path.exists("inventory.json"):
        return

    try:
        with open("inventory.json", "r") as file:
            products_data = json.load(file)

        if not isinstance(products_data, list):
            print("Invalid inventory file format.")
            return

        # Restore objects according to their saved product type
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


# ============================================================
# MENU FUNCTION
# ============================================================

def display_menu():
    print("\n===== Inventory Management System =====")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():
    inventory = Inventory()

    # Load previously saved physical and digital products
    load_inventory(inventory)

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        # OPTION 1: Display all products
        if choice == "1":
            inventory.display_all()

        # OPTION 2: Add a physical or digital product
        elif choice == "2":
            print("\nSelect Product Type:")
            print("1. Physical Product")
            print("2. Digital Product")

            product_type = input("Enter product type (1-2): ")

            if product_type not in ("1", "2"):
                print("Invalid product type.")
                continue

            product_id = input("Enter Product ID: ").strip()
            name = input("Enter Product Name: ").strip()

            if not product_id or not name:
                print("Product ID and name cannot be empty.")
                continue

            if inventory.search_product(product_id) is not None:
                print("Product ID already exists.")
                continue

            try:
                price = float(input("Enter Product Price: "))
                stock = int(input("Enter Stock Quantity: "))

                if not math.isfinite(price) or price < 0 or stock < 0:
                    print("Price and stock must be valid non-negative values.")
                    continue

                if product_type == "1":
                    weight = float(input("Enter Weight (kg): "))

                    if not math.isfinite(weight) or weight < 0:
                        print("Weight must be a valid non-negative number.")
                        continue

                    new_product = PhysicalProduct(
                        product_id, name, price, stock, weight
                    )

                else:
                    download_size = float(input("Enter Download Size (MB): "))

                    if not math.isfinite(download_size) or download_size < 0:
                        print("Download size must be a valid non-negative number.")
                        continue

                    new_product = DigitalProduct(
                        product_id, name, price, stock, download_size
                    )

                inventory.add_product(new_product)

            except ValueError:
                print("Invalid input. Please enter valid numeric values.")

        # OPTION 3: Update stock
        elif choice == "3":
            product_id = input("Enter Product ID to update: ")
            product = inventory.search_product(product_id)

            if product is not None:
                try:
                    new_stock = int(input("Enter New Stock Quantity: "))
                    product.update_stock(new_stock)

                except ValueError:
                    print("Invalid input. Stock must be a whole number.")
            else:
                print("Product not found.")

        # OPTION 4: Search product
        elif choice == "4":
            product_id = input("Enter Product ID to search: ")
            product = inventory.search_product(product_id)

            if product is not None:
                print("\nProduct Found:")
                product.display_information()
                print(product.get_fulfilment_info())

                if isinstance(product, CanBeShipped):
                    print(f"Shipping Cost: ${product.calculate_shipping_cost():.2f}")
            else:
                print("Product not found.")

        # OPTION 5: Save inventory
        elif choice == "5":
            save_inventory(inventory)

        # OPTION 6: Exit
        elif choice == "6":
            print("Exiting Inventory Management System.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
