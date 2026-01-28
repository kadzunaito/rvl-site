from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def t(context, obj, field):
    lang = context.get("lang", "ru")
    value = getattr(obj, f"{field}_{lang}", None)
    if value:
        return value
    return getattr(obj, f"{field}_ru", "")
