
from abc import ABC, abstractmethod
from supplier import Supplier


# ============================================================
# PRODUCT CLASS (ABSTRACT)
# ============================================================

class Product(ABC):
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        supplier: Supplier
    ) -> None:
        self.__product_id: str = product_id
        self.__name: str = name
        self.__price: float = price
        self.__stock: int = stock
        self.__supplier: Supplier = supplier

    def get_product_id(self) -> str:
        return self.__product_id

    def get_price(self) -> float:
        return self.__price

    def get_supplier(self) -> Supplier:
        return self.__supplier

    def to_dict(self) -> dict:
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
            "supplier": self.__supplier.to_dict()
        }

    def update_stock(self, quantity: int) -> None:
        if quantity >= 0:
            self.__stock = quantity
            print("Stock updated successfully.")
        else:
            print("Stock cannot be negative.")

    def display_information(self) -> None:
        print(f"Product ID: {self.__product_id}")
        print(f"Name: {self.__name}")
        print(f"Price: ${self.__price:.2f}")
        print(f"Stock: {self.__stock}")

    def display_supplier_information(self) -> None:
        self.__supplier.display_information()

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass
