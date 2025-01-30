import pytest
from    django.urls import reverse
from shop_app.models import Product


@pytest.mark.django_db
def test_product_add(client, test_data_base):

    """Тест создания товара"""

    url = reverse('add_product')
    response=client.post(url, data={
    'name':"Новый Тестовый товар",
    'description':'Новое Тестовое описание товара',
    'price':'1000',
    'category': '1'
    })

    assert response.status_code == 302

    created_product = Product.objects.last()
    assert created_product.name == 'Новый Тестовый товар'
    assert created_product.description == 'Новое Тестовое описание товара'
    assert created_product.price == 1000
    assert created_product.category.id == 1

