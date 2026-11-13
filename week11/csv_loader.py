
import csv

from inventory import Inventory
from supplier import Supplier
from product_factory import ProductFactory


# ============================================================
# CSV PRODUCT LOADER
# ============================================================

def load_products(
    path: str,
    inventory: Inventory,
    supplier: Supplier
) -> None:
    loaded = 0

    try:
        file = open(path, newline="", encoding="utf-8")

    except FileNotFoundError:
        print(f"Products file not found: {path}")

    else:
        with file:
            reader = csv.reader(file)
            next(reader, None)

            for row_number, row in enumerate(reader, start=2):
                try:
                    product_type, product_id, name, price, stock = row

                    product_price = float(price)
                    product_stock = int(stock)

                    if inventory.find_product(product_id) is not None:
                        raise ValueError("Duplicate product ID.")

                    product = ProductFactory.create(
                        product_type=product_type,
                        product_id=product_id,
                        name=name,
                        price=product_price,
                        stock=product_stock,
                        supplier=supplier
                    )

                    inventory.add_product(product)
                    loaded += 1

                except ValueError as error:
                    print(f"Row {row_number} skipped: {error}")

        print(f"{loaded} products loaded.")

    finally:
        print("Load attempt finished.")
