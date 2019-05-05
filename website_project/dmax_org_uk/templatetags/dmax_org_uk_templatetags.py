from django import template
from django.template.defaultfilters import stringfilter

# Required to register this module with the template tags plumbing
register = template.Library()

@register.filter
@stringfilter
def bold(src_str, bold_str):
    """
    Given a string src_str, returns a modified version with all matches of bold_str wrapped with <strong>...</strong> tags.
    """
    return src_str.replace(bold_str, '<strong>{0}</strong>'.format(bold_str))