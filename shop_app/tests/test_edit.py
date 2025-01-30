import pytest
from shop_app.models import Product

@pytest.mark.django_db
def test_product_detail(client, test_data_base):

    """Тест редактирования карточки товара"""

    product=test_data_base['product']
    product_id=product.id

    url = f'/product/{product_id}/edit_product/'

    # Проверяем, формирование страницы редактирования товара
    response=client.get(url)
    assert response.status_code == 200
    assert 'Редактирование карточки товара' in response.content.decode('utf-8')
    assert 'Тестовый товар' in response.content.decode('utf-8')
    assert 'Тестовая категория' in response.content.decode('utf-8')

    # Проверяем, редактирование товара
    response=client.post(url, data={
    'name':"Отредактированный Тестовый товар",
    'description':'Отредактированное Тестовое описание товара',
    'price':'2000',
    'category': '1'
    })

    assert response.status_code == 302

    created_product = Product.objects.last()
    assert created_product.name == 'Отредактированный Тестовый товар'
    assert created_product.description == 'Отредактированное Тестовое описание товара'
    assert created_product.price == 2000
    assert created_product.category.id == 1



