import pytest
from django.contrib.auth import get_user_model

from request_vars import REQUEST_VARS
from request_vars.decorators import request_cache
from tests.test_app.exceptions import RequestVarsError


def middleware_callback(_):
    REQUEST_VARS.callback = 'test_callback'


@request_cache
def request_cache_fn(val):
    return val


callback = 'tests.test_middleware.middleware_callback'


@pytest.mark.django_db
def test_anonymous(client):
    response = client.get('/test_view/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_logged_in_user(client):
    get_user_model().objects.create_user(
        username='test_user', password='test_password'
    )
    client.login(username='test_user', password='test_password')
    response = client.get('/test_view/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_middleware_callback(client, settings):
    settings.REQUEST_VARS_MIDDLEWARE_CALLBACK = callback
    response = client.get('/test_view/?callback=test_callback')
    assert response.status_code == 200


@pytest.mark.django_db
def test_clear_thread_local(client, settings):
    settings.REQUEST_VARS_MIDDLEWARE_CALLBACK = callback
    client.get('/test_view/?callback=test_callback')
    assert not hasattr(REQUEST_VARS, 'request')
    assert not hasattr(REQUEST_VARS, 'user')
    assert not hasattr(REQUEST_VARS, 'callback')


@pytest.mark.django_db
def test_clear_thread_local_with_exception(client, settings):
    settings.REQUEST_VARS_MIDDLEWARE_CALLBACK = callback
    with pytest.raises(RequestVarsError):
        client.get('/test_view/?callback=test_callback&exception=1')
    assert not hasattr(REQUEST_VARS, 'request')
    assert not hasattr(REQUEST_VARS, 'user')
    assert not hasattr(REQUEST_VARS, 'callback')


@pytest.mark.django_db
def test_request_cache(client):
    response = client.get('/request_cache_view/')
    assert response.status_code == 200


def test_request_cache_without_request():
    # Not cache if no request
    val = request_cache_fn('test')
    assert val == 'test'
    val = request_cache_fn('test1')
    assert val == 'test1'
