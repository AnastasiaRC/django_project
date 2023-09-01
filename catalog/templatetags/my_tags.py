from django import template

register = template.Library()


@register.filter()
def mediapath(value):
    if value:
        return f'/media/product/{value}'
    return '/media/zg.jpeg'


@register.filter()
def mediapath_(value):
    if value:
        return f'/media/{value}'
    return '/media/zgblog.png'
