from django.db.models import Q
from django.views import generic

from notebooks.models import NoteBook


class PagesIndexView(generic.TemplateView):
    template_name = "pages/index.html"


class PagesSearchView(generic.ListView):
    template_name = "pages/search.html"
    model = NoteBook
    context_object_name = "notebooks"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        search_word = self.request.GET.get("q")
        context["search_word"] = search_word
        return context

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = NoteBook.objects.filter(Q(content__icontains=query))
        return object_list
