"""
Протестируйте классы из модуля homework/models.py
"""
import pytest
from models import Product, Cart

@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture()
def cart():
    return Cart()

class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(10)
        assert product.check_quantity(1000)
        assert not product.check_quantity(1001)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        old_quantity = product.quantity
        product.buy(10)
        assert old_quantity == product.quantity + 10

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError) as excinfo:
            product.buy(10000)
        assert excinfo.typename == 'ValueError'


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_to_cart(self, cart,  product):
        cart.add_product(product, 1)
        assert cart.products[product] == 1
        cart.add_product(product, 10)
        assert cart.products[product] == 11


    def test_del_to_card(self, cart , product):
        cart.add_product(product, 10)
        cart.remove_product(product, 9)
        assert cart.products[product] == 1
        cart.remove_product(product, 2)
        assert product not in cart.products.keys()
        cart.add_product(product, 10)
        cart.remove_product(product)
        assert product not in cart.products.keys()


    def test_clear_card(self, cart , product):
        cart.add_product(product, 10)
        cart.clear()
        assert product not in cart.products.keys()


    def test_total_price(self, cart, product):
        cart.add_product(product, 7)
        assert cart.get_total_price() == 100 * 7