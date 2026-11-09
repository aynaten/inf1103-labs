
from product import Product
from order_line import OrderLine


# ============================================================
# ORDER CLASS
# ============================================================

class Order:
    def __init__(self, order_id: str):
        self.order_id: str = order_id
        self.__order_lines: list[OrderLine] = []

    def get_order_lines(self) -> list[OrderLine]:
        return self.__order_lines.copy()

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)
        print("Order line added successfully.")

    def remove_order_line(self, product_id: str) -> bool:
        for order_line in self.__order_lines:
            if order_line.product.get_product_id() == product_id:
                self.__order_lines.remove(order_line)
                print("Order line removed successfully.")
                return True

        print("Order line not found.")
        return False

    def calculate_total(self) -> float:
        total = 0.0

        for order_line in self.__order_lines:
            total += order_line.calculate_subtotal()

        return total

    def display_order(self) -> None:
        print(f"Order ID: {self.order_id}")

        if not self.__order_lines:
            print("This order has no items.")
            return

        for order_line in self.__order_lines:
            product_id = order_line.product.get_product_id()
            subtotal = order_line.calculate_subtotal()

            print(
                f"Product: {product_id} | "
                f"Quantity: {order_line.quantity} | "
                f"Subtotal: ${subtotal:.2f}"
            )

        print(f"Order Total: ${self.calculate_total():.2f}")
