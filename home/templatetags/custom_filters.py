# custom_filters.py
from django import template

register = template.Library()

@register.filter(name='format_date')
def format_date(value, arg='%A, %d %B %Y'):
    return value.strftime(arg)
