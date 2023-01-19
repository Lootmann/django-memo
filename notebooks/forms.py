from django import forms

from notebooks.models import NoteBook


class NoteBookEditForm(forms.ModelForm):
    class Meta:
        model = NoteBook
        fields = ("title", "content")
