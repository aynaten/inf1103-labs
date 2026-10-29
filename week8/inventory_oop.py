
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
# MAIN PROGRAM - TEST INVENTORY CLASS
# ============================================================

def main():
    # Create an empty inventory object
    inventory = Inventory()

    # Create two Product objects
    product1 = Product("P001", "Laptop", 1200.00, 15)
    product2 = Product("P002", "Mouse", 25.50, 40)

    # Add both products to the inventory
    inventory.add_product(product1)
    inventory.add_product(product2)

    # Display all products
    print("\nAll Products:")
    inventory.display_all()

    # Search for a product by its ID
    print("\nSearching for P002:")
    found_product = inventory.search_product("P002")

    if found_product:
        found_product.display_information()
    else:
        print("Product not found.")


if __name__ == "__main__":
    main()
