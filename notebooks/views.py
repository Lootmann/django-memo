from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic

from notebooks.forms import NoteBookEditForm
from notebooks.models import NoteBook


class NoteBookCreateView(generic.View):
    def post(self, request, *args, **kwargs):
        """
        create newbook, and redirect notebooks:edit directly
        """
        newbook = NoteBook.objects.create()
        return redirect(reverse("notebooks:edit", kwargs={"pk": newbook.id}))


class NoteBookEditView(generic.UpdateView):
    template_name = "notebooks/edit.html"
    model = NoteBook
    form_class = NoteBookEditForm
    context_object_name = "notebook"

    def get_success_url(self):
        return reverse("notebooks:edit", kwargs={"pk": self.object.id})
