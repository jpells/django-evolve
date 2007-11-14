from django import template
from django.conf import settings

register = template.Library()

def show_idea(idea):
    return {'MEDIA_URL': settings.MEDIA_URL, 'idea': idea}

register.inclusion_tag('evolve/_idea.html')(show_idea)
