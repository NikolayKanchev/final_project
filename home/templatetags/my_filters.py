from django import template
register = template.Library()


@register.filter
def get_categories(section):
    return section.category_set.filter(section=section).order_by("pk")


@register.filter
def get_photos(child):
    return child.photo_set.filter(child=child).order_by("pk")

