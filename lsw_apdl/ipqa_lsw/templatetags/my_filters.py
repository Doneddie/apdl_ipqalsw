from django import template

register = template.Library()

@register.filter
def section_has_data(data, section_prefix):
    """Check if any field in section has data"""
    return any(v for k,v in data.items() if k.startswith(section_prefix) and v)