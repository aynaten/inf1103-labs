
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
