from django import template

register = template.Library()

@register.filter
def truncchar(value, arg):
    '''
    Truncate text after a certain number of characters
    '''
    if len(value) < arg:
        return value
    else:
        return value[:arg] + '...'
