from django import template
register = template.Library()


@register.filter
def get_categories(section):
    return section.category_set.filter(section=section)
