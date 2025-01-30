import pytest
from shop_app.models import Product, Category




@pytest.fixture
def test_data_base():
    """создаём элементы для тестовой БД"""
    category=Category.objects.create(name="Тестовая категория", description='Тестовое описание категории')
    product = Product.objects.create(name="Тестовый товар", description='Тестовое описание товара', price=10000, category=category)
    return dict(product=product, category=category)


