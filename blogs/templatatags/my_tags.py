from django import template

register = template.Library()


@register.filter()
def mediapath(input_value):
    if input_value:
        return f"/media/{input_value}"
    else:
        return '/static/main/images/lag-60.png'


@register.simple_tag
def mediapath_tag(input_value):
    if input_value:
        return f"/media/{input_value}"
    else:
        return '/static/main/images/lag-60.png'