
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
# MAIN PROGRAM - TEST PRODUCT CLASS
# ============================================================

def main():
    product1 = Product("P001", "Laptop", 1200.00, 15)

    print("Original Product:")
    product1.display_information()

    print("\nUpdating Stock:")
    product1.update_stock(20)

    print("\nUpdated Product:")
    product1.display_information()


if __name__ == "__main__":
    main()
