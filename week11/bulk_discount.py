
from discount_strategy import DiscountStrategy


# ============================================================
# BULK DISCOUNT CLASS
# ============================================================

class BulkDiscount(DiscountStrategy):
    def __init__(
        self,
        threshold: float,
        amount: float
    ) -> None:
        if threshold < 0 or amount < 0:
            raise ValueError("Threshold and amount cannot be negative.")

        self.__threshold: float = threshold
        self.__amount: float = amount

    def apply(self, total: float) -> float:
        if total >= self.__threshold:
            return max(0.0, total - self.__amount)

        return total
