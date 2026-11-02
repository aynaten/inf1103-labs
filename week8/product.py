
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
