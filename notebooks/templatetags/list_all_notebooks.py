from django import template

from notebooks.models import NoteBook

register = template.Library()


@register.inclusion_tag("notebooks/list_notebooks.html")
def render_notebooks():
    return {
        "notebooks": NoteBook.objects.all(),
    }
