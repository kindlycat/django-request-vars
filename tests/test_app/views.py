from request_vars.utils import get_variable, set_variable

from django.http import HttpResponse
from django.shortcuts import render

from tests.test_middleware import request_cache_fn


def test_view(request):
    # test exception
    if request.GET.get('exception'):
        raise Exception

    if request != get_variable('request'):
        raise AssertionError('Bad request value.')
    if request.user != get_variable('user'):
        raise AssertionError('Bad user value.')

    # test callback
    if request.GET.get('callback') and request.GET['callback'] != get_variable(
        'callback'
    ):
        raise AssertionError('Bad callback value.')
    return HttpResponse('')


def request_cache_view(request):
    val = request_cache_fn('test')
    if val != 'test':
        raise AssertionError('Bad request_cache first call value.')
    val = request_cache_fn('test2')
    if val != 'test':
        raise AssertionError('Bad request_cache second call value.')
    return HttpResponse('')


def test_template_tag_view(request, **kwargs):
    set_variable('additional_key', 'additional_value')
    return render(request, kwargs.get('template', 'index.html'))
