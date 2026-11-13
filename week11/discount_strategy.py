
from abc import ABC, abstractmethod


# ============================================================
# DISCOUNT STRATEGY ABSTRACT CLASS
# ============================================================

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total: float) -> float:
        pass
