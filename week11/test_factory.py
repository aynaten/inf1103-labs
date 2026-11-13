
from supplier import Supplier
from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from product_factory import ProductFactory


# ============================================================
# PHASE 3 - FACTORY PATTERN TEST
# ============================================================

def main() -> None:
    supplier = Supplier(
        "S001",
        "Tech Supplies",
        "contact@techsupplies.example"
    )

    print("=== Test 1: Create Physical Product ===")

    physical = ProductFactory.create(
        "physical",
        "P001",
        "Laptop",
        1200.00,
        10,
        supplier,
        weight=2.5
    )

    physical.display_information()

    assert isinstance(physical, PhysicalProduct)
    assert isinstance(physical, Product)

    print("\nPASS: PhysicalProduct created correctly")

    print("\n=== Test 2: Create Digital Product ===")

    digital = ProductFactory.create(
        "digital",
        "D001",
        "Software",
        49.99,
        100,
        supplier,
        download_size=500
    )

    digital.display_information()

    assert isinstance(digital, DigitalProduct)
    assert isinstance(digital, Product)

    print("\nPASS: DigitalProduct created correctly")

    print("\n=== Test 3: Supplier Association ===")

    assert physical.get_supplier() is supplier
    assert digital.get_supplier() is supplier

    print("PASS: Both products use the original Supplier")

    print("\n=== Test 4: Unknown Product Type ===")

    try:
        ProductFactory.create(
            "service",
            "S002",
            "Installation",
            30.00,
            5,
            supplier
        )

    except ValueError as error:
        print(f"Caught expected error: {error}")
        assert str(error) == "Unknown product type: service"

    else:
        raise AssertionError(
            "Factory should reject an unknown product type."
        )

    print("\nALL FACTORY TESTS PASSED")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
