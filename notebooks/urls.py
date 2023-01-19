from django.urls import path

from notebooks.views import NoteBookCreateView, NoteBookEditView

app_name = "notebooks"

urlpatterns = [
    path("create/", NoteBookCreateView.as_view(), name="create"),
    path("edit/<int:pk>/", NoteBookEditView.as_view(), name="edit"),
]
