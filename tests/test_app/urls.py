from django.conf.urls import url

from tests.test_app.views import (
    request_cache_view, test_template_tag_view, test_view
)


urlpatterns = [
    url(r'^test_view/$', test_view),
    url(r'^request_cache_view/$', request_cache_view),
    url(r'^test_django_template_tag/$', test_template_tag_view),
    url(r'^test_jinja_template_tag/$', test_template_tag_view,
        kwargs={'template': 'index.jinja'})
]
