import pytest


@pytest.mark.django_db
def test_product_detail(client, test_data_base):

    """Тест просмотра карточки товара"""

    product=test_data_base['product']
    product_id=product.id
    url = f'/product/{product_id}/'

    # print([x.name for x in Product.objects.all()])

    response=client.get(url)
    assert response.status_code == 200
    assert 'Тестовый товар' in response.content.decode('utf-8')
    assert 'Тестовое описание категории' in response.content.decode('utf-8')
    assert 'Тестовое описание товара' in response.content.decode('utf-8')
