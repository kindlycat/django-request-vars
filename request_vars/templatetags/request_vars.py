from request_vars.utils import get_variable

from django import template


try:
    from django_jinja import library
except ImportError:  # pragma: no cover
    library = None


register = template.Library()

register.simple_tag(get_variable)

if library:
    library.global_function(get_variable)
