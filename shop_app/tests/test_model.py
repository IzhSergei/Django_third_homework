import pytest
from shop_app.models import Category, Product


@pytest.mark.django_db
def test_models(test_data_base):

    """Тестирование моделей"""

    test_category=test_data_base['category']
    test_product=test_data_base['product']

    assert Category.objects.count() == 1
    assert Product.objects.count() == 1
    assert test_category.name == 'Тестовая категория'
    assert test_category.description == 'Тестовое описание категории'
    assert test_product.name == 'Тестовый товар'
    assert test_product.description == 'Тестовое описание товара'
    assert test_product.price == 10000
    assert test_product.category.id == 1
    assert test_product.category.description == 'Тестовое описание категории'






