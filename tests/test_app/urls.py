from django.urls import path

from tests.test_app.views import (
    request_cache_view,
    test_template_tag_view,
    test_view,
)


urlpatterns = [
    path('test_view/', test_view),
    path('request_cache_view/', request_cache_view),
    path('test_django_template_tag/', test_template_tag_view),
    path(
        'test_jinja_template_tag/',
        test_template_tag_view,
        kwargs={'template': 'index.jinja'},
    ),
]
