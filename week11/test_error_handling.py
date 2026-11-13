
from pathlib import Path
from unittest.mock import patch

from input_helpers import get_positive_float
from csv_loader import load_products
from inventory import Inventory
from supplier import Supplier


# ============================================================
# PHASE 5 - ERROR HANDLING TESTS
# ============================================================

def main() -> None:
    print("=== Test 1: Invalid Price Input ===")

    with patch("builtins.input", side_effect=["abc", "-5", "12.50"]):
        price = get_positive_float("Enter price: $")

    print(f"Accepted price: ${price:.2f}")
    assert price == 12.50
    print("PASS: Invalid inputs rejected")

    print("\n=== Test 2: Load Products From CSV ===")

    supplier = Supplier(
        "S001",
        "Tech Supplies",
        "contact@techsupplies.example"
    )

    inventory = Inventory()

    csv_path = Path(__file__).resolve().parent / "products.csv"

    load_products(str(csv_path), inventory, supplier)

    assert len(inventory.get_products()) == 3

    assert inventory.find_product("P001") is not None
    assert inventory.find_product("D001") is not None
    assert inventory.find_product("P003") is not None

    assert inventory.find_product("P002") is None
    assert inventory.find_product("S001") is None

    print("PASS: Three valid products loaded")

    print("\n=== Test 3: Missing CSV File ===")

    missing_path = Path(__file__).resolve().parent / "missing_products.csv"

    assert not missing_path.exists()

    load_products(str(missing_path), Inventory(), supplier)

    print("PASS: Missing file handled without crashing")

    print("\nALL ERROR HANDLING TESTS PASSED")


# ============================================================
# PROGRAM ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
