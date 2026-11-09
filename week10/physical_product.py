
from product import Product
from supplier import Supplier
from can_be_shipped import CanBeShipped


# ============================================================
# PHYSICAL PRODUCT CLASS
# ============================================================

class PhysicalProduct(Product):
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        weight: float,
        supplier: Supplier
    ) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight: float = weight

    def display_information(self) -> None:
        super().display_information()
        print("Product Type: Physical")
        print(f"Weight: {self.__weight} kg")

    def get_fulfilment_info(self) -> str:
        return "This product requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        shipping_rate: float = 5.00
        return self.__weight * shipping_rate

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self.__weight
        return data


# ============================================================
# INTERFACE REGISTRATION
# ============================================================

CanBeShipped.register(PhysicalProduct)
