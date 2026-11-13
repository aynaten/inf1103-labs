
import unittest

from supplier import Supplier
from product_factory import ProductFactory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from order import Order

from no_discount import NoDiscount
from percentage_discount import PercentageDiscount
from bulk_discount import BulkDiscount
from student_discount import StudentDiscount


# ============================================================
# STRATEGY PATTERN TESTS
# ============================================================

class TestStrategyPattern(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier(
            "S001",
            "Tech Supplies",
            "contact@techsupplies.example"
        )

        self.product = ProductFactory.create(
            "physical",
            "P001",
            "Keyboard",
            125.00,
            10,
            self.supplier,
            weight=1.0
        )

        self.order = Order("O001")
        self.order.add_order_line(self.product, 2)

    def test_no_discount(self):
        self.order.set_discount(NoDiscount())
        self.assertEqual(self.order.calculate_total(), 250.00)

    def test_percentage_discount(self):
        self.order.set_discount(PercentageDiscount(10))
        self.assertEqual(self.order.calculate_total(), 225.00)

    def test_bulk_discount(self):
        self.order.set_discount(BulkDiscount(200, 20))
        self.assertEqual(self.order.calculate_total(), 230.00)

    def test_student_discount(self):
        self.order.set_discount(StudentDiscount())
        self.assertEqual(self.order.calculate_total(), 237.50)

    def test_switch_discount(self):
        self.order.set_discount(PercentageDiscount(10))
        self.assertEqual(self.order.calculate_total(), 225.00)

        self.order.set_discount(NoDiscount())
        self.assertEqual(self.order.calculate_total(), 250.00)


# ============================================================
# FACTORY PATTERN TESTS
# ============================================================

class TestFactoryPattern(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier(
            "S001",
            "Tech Supplies",
            "contact@techsupplies.example"
        )

    def test_create_physical_product(self):
        product = ProductFactory.create(
            "physical",
            "P001",
            "Laptop",
            1200.00,
            10,
            self.supplier,
            weight=2.5
        )

        self.assertIsInstance(product, PhysicalProduct)

    def test_create_digital_product(self):
        product = ProductFactory.create(
            "digital",
            "D001",
            "Software",
            49.99,
            100,
            self.supplier,
            download_size=500
        )

        self.assertIsInstance(product, DigitalProduct)

    def test_unknown_product_type(self):
        with self.assertRaises(ValueError):
            ProductFactory.create(
                "service",
                "S001",
                "Installation",
                30.00,
                5,
                self.supplier
            )


# ============================================================
# PRODUCT VALIDATION TESTS
# ============================================================

class TestProductValidation(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier(
            "S001",
            "Tech Supplies",
            "contact@techsupplies.example"
        )

    def test_zero_price_rejected(self):
        with self.assertRaises(ValueError):
            ProductFactory.create(
                "physical",
                "P001",
                "Keyboard",
                0.0,
                10,
                self.supplier,
                weight=1.0
            )

    def test_negative_price_rejected(self):
        with self.assertRaises(ValueError):
            ProductFactory.create(
                "digital",
                "D001",
                "Software",
                -20.00,
                10,
                self.supplier,
                download_size=500
            )

    def test_negative_stock_rejected(self):
        with self.assertRaises(ValueError):
            ProductFactory.create(
                "physical",
                "P002",
                "Mouse",
                25.00,
                -5,
                self.supplier,
                weight=0.2
            )

    def test_zero_order_quantity_rejected(self):
        product = ProductFactory.create(
            "physical",
            "P003",
            "Monitor",
            250.00,
            10,
            self.supplier,
            weight=3.0
        )

        order = Order("O001")

        with self.assertRaises(ValueError):
            order.add_order_line(product, 0)
