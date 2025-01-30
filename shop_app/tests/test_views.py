import pytest
from    django.urls import reverse



# Create your tests here.
def test_shop_start(client):

    """Тест вывода стартовой странички"""

    url = reverse('shop_start')
    response = client.get(url)
    assert response.status_code == 200
    assert 'Добро пожаловать' in response.content.decode('utf-8')


@pytest.mark.django_db
def test_category_list(client, test_data_base):

    """Тест вывода списка категорий"""

    url = reverse('category_list')
    response = client.get(url)
    assert response.status_code == 200
    assert 'добавить категорию' in response.content.decode('utf-8')
    assert 'Категории' in response.content.decode('utf-8')
    assert 'Тестовая категория' in response.content.decode('utf-8')


@pytest.mark.django_db
def test_products_list(client, test_data_base):

    """Тест вывода списка товаров"""

    url = reverse('products_list')
    response = client.get(url)
    assert response.status_code == 200
    assert 'добавить товар' in response.content.decode('utf-8')
    assert 'Товары' in response.content.decode('utf-8')
    assert 'Тестовый товар' in response.content.decode('utf-8')
    assert 'Тестовое описание товара' in response.content.decode('utf-8')

