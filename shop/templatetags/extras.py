from django import template

register = template.Library()

@register.filter
def make_chunks(value, chunk_size):
    """ Break a list into chunks of size 'chunk_size' """
    chunk_size = int(chunk_size)
    return [value[i:i + chunk_size] for i in range(0, len(value), chunk_size)]
