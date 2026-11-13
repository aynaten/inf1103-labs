
from discount_strategy import DiscountStrategy


# ============================================================
# PERCENTAGE DISCOUNT CLASS
# ============================================================

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float) -> None:
        if not 0 <= percentage <= 100:
            raise ValueError("Percentage must be between 0 and 100.")

        self.__percentage: float = percentage

    def apply(self, total: float) -> float:
        return total * (1 - self.__percentage / 100)
