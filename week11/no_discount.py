
from discount_strategy import DiscountStrategy


# ============================================================
# NO DISCOUNT CLASS
# ============================================================

class NoDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total
