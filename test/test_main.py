import unittest
from src.main import (
    Product,
    Smartphone,
    LawnGrass,
    Category,



class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product1 = Product("Товар 1", "Описание товара 1", 100.0, 10)
        self.product2 = Product("Товар 2", "Описание товара 2", 200.0, 5)

    def test_addition_same_type(self):
        self.assertEqual(self.product1 + self.product2, 300.0)

    def test_addition_different_type(self):
        with self.assertRaises(TypeError):
            self.product1 + "Не продукт"


class TestSmartphone(unittest.TestCase):
    def setUp(self):
        self.smartphone = Smartphone(
            "Samsung Galaxy S23", "Описание", 100000.0, 5, 95.0, "S23", 256, "Серый"
        )

    def test_smartphone_attributes(self):
        self.assertEqual(self.smartphone.name, "Samsung Galaxy S23")
        self.assertEqual(self.smartphone.description, "Описание")
        self.assertEqual(self.smartphone.price, 100000.0)
        self.assertEqual(self.smartphone.quantity, 5)
        self.assertEqual(self.smartphone.efficiency, 95.0)
        self.assertEqual(self.smartphone.model, "S23")
        self.assertEqual(self.smartphone.memory, 256)
        self.assertEqual(self.smartphone.color, "Серый")

    class TestLawnGrass(unittest.TestCase):
        def setUp(self):
            self.grass = LawnGrass(
                "Газонная трава", "Описание", 500.0, 20, "Россия", "7 дней", "Зеленый"
            )

        def test_lawn_grass_attributes(self):
            self.assertEqual(self.grass.name, "Газонная трава")
            self.assertEqual(self.grass.description, "Описание")
            self.assertEqual(self.grass.price, 500.0)
            self.assertEqual(self.grass.quantity, 20)
            self.assertEqual(self.grass.country, "Россия")
            self.assertEqual(self.grass.germination_period, "7 дней")
            self.assertEqual(self.grass.color, "Зеленый")

    class TestCategory(unittest.TestCase):
        def setUp(self):
            # Сбрасываем product_count перед каждым тестом
            Category.product_count = 0
            self.category = Category("Смартфоны", "Описание категории", [])
            self.smartphone = Smartphone(
                "Samsung Galaxy S23", "Описание", 100000.0, 5, 95.0, "S23", 256, "Серый"
            )

            def test_add_product(self):
                self.category.add_product(self.smartphone)
                self.assertIn(self.smartphone, self.category.products)

            def test_add_invalid_product(self):
                with self.assertRaises(TypeError):
                    self.category.add_product("Не продукт")

            def test_product_count(self):
                self.assertEqual(
                    Category.product_count, 0
                )  # Проверяем, что изначально 0
                self.category.add_product(self.smartphone)
                self.assertEqual(
                    Category.product_count, 1
                )  # Проверяем, что после добавления 1

        if __name__ == "__main__":
            unittest.main()
