import pytest
from shop_app.models import Product

@pytest.mark.django_db
def test_product_delete(client, test_data_base):

    """Тест удаления товара"""

    product=test_data_base['product']
    product_id=product.id

    url = f'/product/{product_id}/delete/'

    # Проверяем, формирование страницы удаления товара
    response=client.get(url)
    assert response.status_code == 200
    assert 'подтвердите удаление товара' in response.content.decode('utf-8')
    assert 'Тестовый товар' in response.content.decode('utf-8')
    assert 'Тестовое описание товара' in response.content.decode('utf-8')
    assert 'Удалить' in response.content.decode('utf-8')
    assert 'Отмена' in response.content.decode('utf-8')


    response = client.post(url)

    # Проверяем, что объект был удален
    assert response.status_code == 302
    assert not Product.objects.filter(pk=product_id).exists()  # объект не существует

