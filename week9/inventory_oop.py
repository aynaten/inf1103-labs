
import json
import os
import math
from abc import ABC, abstractmethod


# ============================================================
# PRODUCT CLASS (ABSTRACT)
# ============================================================

class Product(ABC):
    # Initialise a product with its ID, name, price and stock
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    # Return the product ID without directly accessing
    # the private attribute from outside the class
    def get_product_id(self):
        return self.__product_id

    # Convert Product attributes into a dictionary for JSON saving
    # This will be extended in Phase 5
    def to_dict(self):
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock
        }

    # Update the stock quantity of this product
    def update_stock(self, quantity):
        if quantity >= 0:
            self.__stock = quantity
            print("Stock updated successfully.")
        else:
            print("Stock cannot be negative.")

    # Display the product's common information
    def display_information(self):
        print(f"Product ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")

    # Abstract method that all specialised products must implement
    @abstractmethod
    def get_fulfilment_info(self):
        pass


# ============================================================
# CAN BE SHIPPED INTERFACE
# ============================================================

class CanBeShipped(ABC):

    # Require implementing classes to calculate shipping costs
    @abstractmethod
    def calculate_shipping_cost(self):
        pass


# ============================================================
# PHYSICAL PRODUCT CLASS
# ============================================================

class PhysicalProduct(Product):
    # Initialise a physical product with an additional weight
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    # Override the parent method to display additional information
    def display_information(self):
        super().display_information()
        print("Product Type: Physical")
        print(f"Weight: {self.__weight} kg")

    # Explain how a physical product is delivered
    def get_fulfilment_info(self):
        return "This product requires physical shipping."

    # Calculate shipping using $5 per kilogram
    def calculate_shipping_cost(self):
        shipping_rate = 5.00
        return self.__weight * shipping_rate


# ============================================================
# DIGITAL PRODUCT CLASS
# ============================================================

class DigitalProduct(Product):
    # Initialise a digital product with an additional download size
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    # Override the parent method to display additional information
    def display_information(self):
        super().display_information()
        print("Product Type: Digital")
        print(f"Download Size: {self.__download_size} MB")

    # Explain how a digital product is delivered
    def get_fulfilment_info(self):
        return "This product is delivered digitally."


# ============================================================
# INTERFACE REGISTRATION
# ============================================================

CanBeShipped.register(PhysicalProduct)


# ============================================================
# INVENTORY CLASS
# ============================================================

class Inventory:
    # Initialise an empty inventory
    def __init__(self):
        self.__products = []

    # Return the collection of products
    def get_products(self):
        return self.__products

    # Add a Product object to the inventory
    def add_product(self, product):
        # Prevent duplicate product IDs
        if self.search_product(product.get_product_id()) is not None:
            print("Product ID already exists.")
            return

        self.__products.append(product)
        print("Product added successfully.")

    # Search for a product using its product ID
    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    # Display all products in the inventory
    def display_all(self):
        if not self.__products:
            print("Inventory is empty.")
            return

        for product in self.__products:
            print("--------------------")
            product.display_information()
            print(product.get_fulfilment_info())

            # Only physical products have shipping costs
            if isinstance(product, CanBeShipped):
                print(f"Shipping Cost: ${product.calculate_shipping_cost():.2f}")


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
    # Create an empty Inventory object
    inventory = Inventory()

    # No JSON loading yet - this will be added in Phase 5

    # Keep displaying the menu until the user exits
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        # OPTION 1: Display all products
        if choice == "1":
            inventory.display_all()

        # OPTION 2: Add a new physical or digital product
        elif choice == "2":
            print("\nSelect Product Type:")
            print("1. Physical Product")
            print("2. Digital Product")

            product_type = input("Enter product type (1-2): ")

            # Validate the selected product type
            if product_type not in ("1", "2"):
                print("Invalid product type.")
                continue

            # Collect common product information
            product_id = input("Enter Product ID: ").strip()
            name = input("Enter Product Name: ").strip()

            # Validate the product ID and name
            if not product_id or not name:
                print("Product ID and name cannot be empty.")
                continue

            # Prevent duplicate product IDs
            if inventory.search_product(product_id) is not None:
                print("Product ID already exists.")
                continue

            try:
                # Convert price and stock to the correct data types
                price = float(input("Enter Product Price: "))
                stock = int(input("Enter Stock Quantity: "))

                # Ensure values are valid and non-negative
                if not math.isfinite(price) or price < 0 or stock < 0:
                    print("Price and stock must be valid non-negative values.")
                    continue

                # Create a PhysicalProduct object
                if product_type == "1":
                    weight = float(input("Enter Weight (kg): "))

                    if not math.isfinite(weight) or weight < 0:
                        print("Weight must be a valid non-negative number.")
                        continue

                    new_product = PhysicalProduct(
                        product_id, name, price, stock, weight
                    )

                # Create a DigitalProduct object
                else:
                    download_size = float(input("Enter Download Size (MB): "))

                    if not math.isfinite(download_size) or download_size < 0:
                        print("Download size must be a valid non-negative number.")
                        continue

                    new_product = DigitalProduct(
                        product_id, name, price, stock, download_size
                    )

                # Add the newly created object to Inventory
                inventory.add_product(new_product)

            except ValueError:
                print("Invalid input. Please enter valid numeric values.")

        # OPTION 3: Update stock quantity
        elif choice == "3":
            product_id = input("Enter Product ID to update: ")

            # Search for the existing product
            product = inventory.search_product(product_id)

            if product is not None:
                try:
                    new_stock = int(input("Enter New Stock Quantity: "))
                    product.update_stock(new_stock)

                except ValueError:
                    print("Invalid input. Stock must be a whole number.")
            else:
                print("Product not found.")

        # OPTION 4: Search for a product
        elif choice == "4":
            product_id = input("Enter Product ID to search: ")

            # Search the inventory for the product
            product = inventory.search_product(product_id)

            if product is not None:
                print("\nProduct Found:")
                product.display_information()
                print(product.get_fulfilment_info())

                # Only display shipping cost for physical products
                if isinstance(product, CanBeShipped):
                    print(f"Shipping Cost: ${product.calculate_shipping_cost():.2f}")
            else:
                print("Product not found.")

        # OPTION 5: Save inventory (coming in Phase 5)
        elif choice == "5":
            print("JSON saving will be implemented in Phase 5.")

        # OPTION 6: Exit the application
        elif choice == "6":
            print("Exiting Inventory Management System.")
            break

        # Handle invalid menu choices
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
