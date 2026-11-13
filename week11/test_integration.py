
import tempfile
from pathlib import Path

import file_handler
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order


# ============================================================
# PHASE 5 - INTEGRATION TEST
# ============================================================

def main() -> None:
    supplier = Supplier(
        "S001",
        "Tech Supplies",
        "contact@techsupplies.example"
    )

    laptop = PhysicalProduct(
        "P001", "Laptop", 1200.00, 10, 2.5, supplier
    )

    software = DigitalProduct(
        "D001", "Software", 49.99, 100, 500, supplier
    )

    inventory = Inventory()
    inventory.add_product(laptop)
    inventory.add_product(software)

    order = Order("O001")
    order.add_order_line(laptop, 2)
    order.add_order_line(software, 3)

    orders = [order]

    print("\n=== Test 1: Original Order Total ===")
    assert round(order.calculate_total(), 2) == 2549.97
    print("PASS: Original total is $2549.97")

    original_path = file_handler.FILE_NAME

    try:
        with tempfile.TemporaryDirectory() as directory:
            file_handler.FILE_NAME = Path(directory) / "inventory.json"

            print("\n=== Test 2: Save JSON ===")
            file_handler.save_inventory(inventory, orders)
            assert file_handler.FILE_NAME.exists()
            print("PASS: JSON file created")

            print("\n=== Test 3: Load JSON ===")
            loaded_inventory = Inventory()
            loaded_orders: list[Order] = []
            loaded_suppliers: dict[str, Supplier] = {}

            file_handler.load_inventory(
                loaded_inventory,
                loaded_orders,
                loaded_suppliers
            )

            assert len(loaded_inventory.get_products()) == 2
            assert len(loaded_orders) == 1
            assert len(loaded_suppliers) == 1
            print("PASS: Products, orders and suppliers restored")

            print("\n=== Test 4: Supplier Association ===")

            loaded_laptop = loaded_inventory.find_product("P001")
            loaded_software = loaded_inventory.find_product("D001")

            assert loaded_laptop is not None
            assert loaded_software is not None

            assert (
                loaded_laptop.get_supplier()
                is loaded_software.get_supplier()
            )

            print("PASS: Both products share the same Supplier")

            print("\n=== Test 5: Product Subclasses ===")
            assert isinstance(loaded_laptop, PhysicalProduct)
            assert isinstance(loaded_software, DigitalProduct)
            print("PASS: Correct subclasses restored")

            print("\n=== Test 6: Order Composition ===")
            loaded_order = loaded_orders[0]

            assert round(loaded_order.calculate_total(), 2) == 2549.97

            assert (
                loaded_order.get_order_lines()[0].product
                is loaded_laptop
            )

            print("PASS: Order total and Product reference restored")

    finally:
        file_handler.FILE_NAME = original_path

    print("\nALL PHASE 5 TESTS PASSED")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
