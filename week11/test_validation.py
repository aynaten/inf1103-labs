
from supplier import Supplier
from product_factory import ProductFactory
from order import Order


# ============================================================
# VALIDATION TEST HELPER
# ============================================================

def expect_value_error(test_name: str, action) -> None:
    try:
        action()

    except ValueError as error:
        print(f"PASS: {test_name}")
        print(f"Error message: {error}")

    else:
        raise AssertionError(
            f"FAIL: {test_name} should raise ValueError."
        )


# ============================================================
# PHASE 4 - VALIDATION TESTS
# ============================================================

def main() -> None:
    supplier = Supplier(
        "S001",
        "Tech Supplies",
        "contact@techsupplies.example"
    )

    print("=== Test 1: Zero Product Price ===")

    expect_value_error(
        "Zero price rejected",
        lambda: ProductFactory.create(
            "physical", "P001", "Keyboard",
            0.0, 10, supplier, weight=1.0
        )
    )

    print("\n=== Test 2: Negative Product Price ===")

    expect_value_error(
        "Negative price rejected",
        lambda: ProductFactory.create(
            "digital", "D001", "Software",
            -20.0, 100, supplier, download_size=500
        )
    )

    print("\n=== Test 3: Negative Stock ===")

    expect_value_error(
        "Negative stock rejected",
        lambda: ProductFactory.create(
            "physical", "P002", "Mouse",
            25.0, -5, supplier, weight=0.2
        )
    )

    print("\n=== Test 4: Digital Product Stock Rule ===")

    expect_value_error(
        "DigitalProduct follows Product validation",
        lambda: ProductFactory.create(
            "digital", "D002", "Photo Editor",
            49.90, -1, supplier, download_size=100
        )
    )

    print("\n=== Test 5: Valid Product ===")

    product = ProductFactory.create(
        "physical", "P003", "Monitor",
        250.00, 10, supplier, weight=3.0
    )

    assert product.get_price() == 250.00
    print("PASS: Valid product created")

    print("\n=== Test 6: Invalid Stock Update ===")

    expect_value_error(
        "Negative stock update rejected",
        lambda: product.update_stock(-10)
    )

    print("\n=== Test 7: Zero Order Quantity ===")

    order = Order("O001")

    expect_value_error(
        "Zero order quantity rejected",
        lambda: order.add_order_line(product, 0)
    )

    print("\n=== Test 8: Negative Order Quantity ===")

    expect_value_error(
        "Negative order quantity rejected",
        lambda: order.add_order_line(product, -2)
    )

    print("\n=== Test 9: Valid Order Quantity ===")

    order.add_order_line(product, 2)

    assert order.calculate_total() == 500.00
    print("PASS: Order total is $500.00")

    print("\nALL VALIDATION TESTS PASSED")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
