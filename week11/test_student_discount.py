
from supplier import Supplier
from physical_product import PhysicalProduct
from order import Order
from student_discount import StudentDiscount
from no_discount import NoDiscount


# ============================================================
# PHASE 2 - STUDENT DISCOUNT TEST
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

    print("\n=== Test 1: Original Total ===")
    print(f"Total: ${order.calculate_total():.2f}")
    assert order.calculate_total() == 250.00

    print("\n=== Test 2: Student Discount ===")
    order.set_discount(StudentDiscount())
    print(f"Total: ${order.calculate_total():.2f}")
    assert order.calculate_total() == 237.50

    print("\n=== Test 3: Change Back to No Discount ===")
    order.set_discount(NoDiscount())
    print(f"Total: ${order.calculate_total():.2f}")
    assert order.calculate_total() == 250.00

    print("\n=== Test 4: Shared Discount Strategy ===")
    shared_discount = StudentDiscount()

    order_a = Order("O002", shared_discount)
    order_b = Order("O003", shared_discount)

    print(
        "Both orders share the same strategy:",
        order_a.discount is order_b.discount
    )

    assert order_a.discount is order_b.discount

    print("\nALL STUDENT DISCOUNT TESTS PASSED")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
