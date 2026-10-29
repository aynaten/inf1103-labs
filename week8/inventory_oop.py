
import json
import os

# ============================================================
# PRODUCT CLASS
# ============================================================

class Product:
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

    # Display the product's information
    def display_information(self):
        print(f"Product ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")


# ============================================================
# INVENTORY CLASS
# ============================================================

class Inventory:
    # Initialise an empty inventory
    def __init__(self):
        self.__products = []

    # Return the collection of products for JSON saving
    def get_products(self):
        return self.__products

    # Add a Product object to the inventory
    def add_product(self, product):
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


# ============================================================
# FILE HANDLING
# Loads and saves inventory data using JSON
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

    # Load previously saved products when the program starts
    load_inventory(inventory)

    # Keep displaying the menu until the user exits
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        # OPTION 1: Display all products
        if choice == "1":
            inventory.display_all()

        # OPTION 2: Add a new product
        elif choice == "2":
            # Collect product details from the user
            product_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")

            try:
                # Convert input into appropriate data types
                price = float(input("Enter Product Price: "))
                stock = int(input("Enter Stock Quantity: "))

                # Check that the values are valid
                if price < 0 or stock < 0:
                    print("Price and stock cannot be negative.")

                # Prevent duplicate product IDs
                elif inventory.search_product(product_id) is not None:
                    print("Product ID already exists.")

                else:
                    # Create a new Product object
                    new_product = Product(product_id, name, price, stock)

                    # Add the Product object to Inventory
                    inventory.add_product(new_product)

            except ValueError:
                print("Invalid input. Price must be a number and stock must be a whole number.")

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
            # Ask the user which product to search for
            product_id = input("Enter Product ID to search: ")

            # Search the inventory for the product
            product = inventory.search_product(product_id)

            # Display the product if found
            if product is not None:
                print("\nProduct Found:")
                product.display_information()
            else:
                print("Product not found.")

        # OPTION 5: Save inventory to JSON
        elif choice == "5":
            save_inventory(inventory)

        # OPTION 6: Exit program
        elif choice == "6":
            print("Exiting Inventory Management System.")
            break

        # Handle invalid menu selections
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
