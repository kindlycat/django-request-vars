from django import template

from request_vars.utils import get_variable


register = template.Library()

register.simple_tag(get_variable)
