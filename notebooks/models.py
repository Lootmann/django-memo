from django.db import models


class NoteBook(models.Model):
    class Meta:
        db_table = "notebook"
        verbose_name = "notebook"
        verbose_name_plural = "notebooks"

    title = models.CharField(max_length=100, default="no title", blank=True)
    content = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.title
