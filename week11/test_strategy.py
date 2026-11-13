
from supplier import Supplier
from physical_product import PhysicalProduct
from order import Order
from no_discount import NoDiscount
from percentage_discount import PercentageDiscount
from bulk_discount import BulkDiscount


# ============================================================
# PHASE 1 - STRATEGY PATTERN TEST
# ============================================================

def main() -> None:
    supplier = Supplier(
        "S001",
        "Tech Supplies",
        "contact@techsupplies.example"
    )

    product = PhysicalProduct(
        "P001",
        "Keyboard",
        125.00,
        10,
        1.0,
        supplier
    )

    order = Order("O001")
    order.add_order_line(product, 2)

    print("\n=== Test 1: No Discount ===")
    order.set_discount(NoDiscount())
    print(f"Total: ${order.calculate_total():.2f}")
    assert order.calculate_total() == 250.00

    print("\n=== Test 2: Bulk Discount ===")
    order.set_discount(BulkDiscount(200, 20))
    print(f"Total: ${order.calculate_total():.2f}")
    assert order.calculate_total() == 230.00

    print("\n=== Test 3: Percentage Discount ===")
    order.set_discount(PercentageDiscount(10))
    print(f"Total: ${order.calculate_total():.2f}")
    assert order.calculate_total() == 225.00

    print("\n=== Test 4: Change Discount Again ===")
    order.set_discount(NoDiscount())
    print(f"Total: ${order.calculate_total():.2f}")
    assert order.calculate_total() == 250.00

    print("\nALL STRATEGY TESTS PASSED")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
