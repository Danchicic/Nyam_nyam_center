from django import template
from django.core.handlers.wsgi import WSGIRequest

register = template.Library()


@register.filter
def unparse_dish_name(field):
    if isinstance(field, WSGIRequest):
        return field
    return field.replace(' ', '_').replace(',', '_')
