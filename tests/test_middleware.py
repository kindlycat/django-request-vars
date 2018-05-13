from django.contrib.auth.models import User
from django.test import TestCase
from django.test.utils import override_settings

from request_vars import REQUEST_VARS
from request_vars.decorators import request_cache


def middleware_callback(request):
    REQUEST_VARS.callback = 'test_callback'


@request_cache
def request_cache_fn(val):
    return val


class MiddlewareTestCase(TestCase):
    callback = 'tests.test_middleware.middleware_callback'

    def test_anonymous(self):
        response = self.client.get('/test_view/')
        self.assertEqual(response.status_code, 200)

    def test_logged_in_user(self):
        User.objects.create_user(username='test_user',
                                 password='test_password')
        self.client.login(username='test_user', password='test_password')
        response = self.client.get('/test_view/')
        self.assertEqual(response.status_code, 200)

    @override_settings(REQUEST_VARS_MIDDLEWARE_CALLBACK=callback)
    def test_middleware_callback(self):
        response = self.client.get('/test_view/?callback=test_callback')
        self.assertEqual(response.status_code, 200)

    @override_settings(REQUEST_VARS_MIDDLEWARE_CALLBACK=callback)
    def test_clear_thread_local(self):
        self.client.get('/test_view/?callback=test_callback')
        self.assertFalse(hasattr(REQUEST_VARS, 'request'))
        self.assertFalse(hasattr(REQUEST_VARS, 'user'))
        self.assertFalse(hasattr(REQUEST_VARS, 'callback'))

    @override_settings(REQUEST_VARS_MIDDLEWARE_CALLBACK=callback)
    def test_clear_thread_local_with_exception(self):
        with self.assertRaises(Exception):
            self.client.get('/test_view/?callback=test_callback&exception=1')
        self.assertFalse(hasattr(REQUEST_VARS, 'request'))
        self.assertFalse(hasattr(REQUEST_VARS, 'user'))
        self.assertFalse(hasattr(REQUEST_VARS, 'callback'))

    def test_request_cache(self):
        response = self.client.get('/request_cache_view/')
        self.assertEqual(response.status_code, 200)

    def test_request_cache_without_request(self):
        # Not cache if no request
        val = request_cache_fn('test')
        self.assertEqual(val, 'test')
        val = request_cache_fn('test1')
        self.assertEqual(val, 'test1')
