
import json
from pathlib import Path

from supplier import Supplier
from product_factory import ProductFactory
from inventory import Inventory
from order import Order


# ============================================================
# FILE CONFIGURATION
# ============================================================

FILE_NAME = Path("inventory.json")


# ============================================================
# SAVE INVENTORY AND ORDERS
# ============================================================

def save_inventory(
    inventory: Inventory,
    orders: list[Order]
) -> None:
    products_data = [
        product.to_dict()
        for product in inventory.get_products()
    ]

    orders_data = []

    for order in orders:
        order_data = {
            "order_id": order.order_id,
            "order_lines": []
        }

        for line in order.get_order_lines():
            order_data["order_lines"].append({
                "product_id": line.product.get_product_id(),
                "quantity": line.quantity
            })

        orders_data.append(order_data)

    data = {
        "products": products_data,
        "orders": orders_data
    }

    try:
        with FILE_NAME.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print("Inventory and orders saved successfully.")

    except OSError as error:
        print(f"Error saving file: {error}")


# ============================================================
# LOAD INVENTORY AND ORDERS
# ============================================================

def load_inventory(
    inventory: Inventory,
    orders: list[Order],
    suppliers: dict[str, Supplier]
) -> None:
    if not FILE_NAME.exists():
        print("No saved inventory found. Starting with an empty inventory.")
        return

    try:
        with FILE_NAME.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            print("Unsupported inventory file format.")
            return

        products_data = data.get("products", [])
        orders_data = data.get("orders", [])

        for item in products_data:
            supplier_data = item["supplier"]
            supplier_id = supplier_data["supplier_id"]

            if supplier_id not in suppliers:
                suppliers[supplier_id] = Supplier(
                    supplier_id,
                    supplier_data["name"],
                    supplier_data["contact_email"]
                )

            supplier = suppliers[supplier_id]

            product = ProductFactory.create(
                product_type=item["type"],
                product_id=item["id"],
                name=item["name"],
                price=item["price"],
                stock=item["stock"],
                supplier=supplier,
                weight=item.get("weight", 0.0),
                download_size=item.get("download_size", 0.0)
            )

            inventory.add_product(product)

        for order_data in orders_data:
            order = Order(order_data["order_id"])

            for line_data in order_data["order_lines"]:
                product = inventory.find_product(
                    line_data["product_id"]
                )

                if product is not None:
                    order.add_order_line(
                        product,
                        line_data["quantity"]
                    )
                else:
                    print(
                        "Skipping missing product in order: "
                        f"{line_data['product_id']}"
                    )

            orders.append(order)

        print("Inventory and orders loaded successfully.")

    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        print(f"Error loading inventory: {error}")
