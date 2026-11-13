
from discount_strategy import DiscountStrategy


# ============================================================
# STUDENT DISCOUNT CLASS
# ============================================================

class StudentDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total * 0.95
