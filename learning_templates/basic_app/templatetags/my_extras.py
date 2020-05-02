from django import template

register = template.Library()

@register.filter('cut')
def cut(value, arg):
    """
    This cuts out all values of 'arg' from the string
    """
    return value.replace(arg, '')
#
# register.filter('cut', cut)

# @register.filter
# def cutout(value, arg):
#     return value.replace(arg, '')
