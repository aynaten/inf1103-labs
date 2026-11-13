
from product import Product
from can_be_shipped import CanBeShipped


# ============================================================
# INVENTORY CLASS
# ============================================================

class Inventory:
    def __init__(self) -> None:
        self.__products: list[Product] = []

    def get_products(self) -> list[Product]:
        return self.__products.copy()

    def add_product(self, product: Product) -> None:
        if self.find_product(product.get_product_id()) is not None:
            print("Product ID already exists.")
            return

        self.__products.append(product)
        print("Product added successfully.")

    def remove_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.get_product_id() == product_id:
                self.__products.remove(product)
                print("Product removed successfully.")
                return product

        print("Product not found.")
        return None

    def find_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product

        return None

    def search_product(self, product_id: str) -> Product | None:
        return self.find_product(product_id)

    def display_all(self) -> None:
        if not self.__products:
            print("Inventory is empty.")
            return

        for product in self.__products:
            product.display_information()
            print(product.get_fulfilment_info())

            if isinstance(product, CanBeShipped):
                print(
                    f"Shipping Cost: ${product.calculate_shipping_cost():.2f}"
                )

            print("-" * 40)
