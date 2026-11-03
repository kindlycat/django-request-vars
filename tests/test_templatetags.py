import pytest
from django.contrib.auth import get_user_model


@pytest.mark.django_db
def test_django_template(client):
    get_user_model().objects.create_user(
        username='test_user', password='test_password'
    )
    client.login(username='test_user', password='test_password')
    response = client.get('/test_django_template_tag/')
    assert b'test_user' in response.content
    assert b'additional_value' in response.content
    assert b'default_value' in response.content


@pytest.mark.django_db
def test_jinja_template(client):
    get_user_model().objects.create_user(
        username='test_user', password='test_password'
    )
    client.login(username='test_user', password='test_password')
    response = client.get('/test_jinja_template_tag/')
    assert b'test_user' in response.content
    assert b'additional_value' in response.content
    assert b'default_value' in response.content
