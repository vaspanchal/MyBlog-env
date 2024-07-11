# create custom filter to convert the content into markdown

from django import template
import markdown
from django.utils.safestring import mark_safe # it tells django this is safe for rendering


register = template.Library() # library is a class for registering template tags 

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text, extensions=['markdown.extensions.extra']))