from django.contrib import admin

from notebooks.models import NoteBook


class NoteBookAdmin(admin.ModelAdmin):
    model = NoteBook
    list_display = ["title", "content"]


admin.site.register(NoteBook, NoteBookAdmin)
