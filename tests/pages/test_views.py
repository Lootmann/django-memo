import pytest
from django.db.models import Q
from django.urls import reverse
from pytest_django import asserts

from notebooks.models import NoteBook


def create_search_url(url, query) -> str:
    # a search url is like `/pages/search/?q=hoge`
    return f"{url}?q={query}"


@pytest.mark.django_db
class TestPagesSearchView:
    @pytest.fixture(autouse=True)
    def initial(self, client):
        self.note = NoteBook.objects.create(title="note1", content="zzz")
        NoteBook.objects.create(title="note2", content="hage")
        NoteBook.objects.create(title="note3", content="hige")

        url = create_search_url(url=reverse("pages:search"), query="zzz")
        self.response = client.get(url)

    def test_status_code(self):
        assert self.response.status_code == 200

    def test_template_used(self):
        asserts.assertTemplateUsed(self.response, "base.html")
        asserts.assertTemplateUsed(self.response, "pages/search.html")

    def test_search_word(self):
        assert self.response.context["search_word"] == "zzz"

    def test_search_query(self):
        word = self.response.context["search_word"]
        query = NoteBook.objects.filter(Q(content__icontains=word))

        assert len(query) == 1
        assert query[0] == NoteBook.objects.get(pk=self.note.id)
