import pytest
from django.urls import reverse
from pytest_django import asserts

from notebooks.models import NoteBook


@pytest.mark.django_db
class TestNotebookCreateView:
    @pytest.fixture(autouse=True)
    def initial(self, client):
        url = reverse("notebooks:create")
        self.response = client.post(url)
        self.new_notebook = NoteBook.objects.last()

    def test_status_code(self):
        asserts.assertRedirects(
            self.response,
            reverse("notebooks:edit", kwargs={"pk": self.new_notebook.id}),
            status_code=302,
        )


@pytest.mark.django_db
class TestNotebookEditViewGET:
    @pytest.fixture(autouse=True)
    def initial(self, client):
        self.notebook = NoteBook.objects.create(title="new book", content="hello world :^)")
        self.response = client.get(reverse("notebooks:edit", kwargs={"pk": self.notebook.id}))

    def test_status_code(self):
        assert self.response.status_code == 200


@pytest.mark.django_db
class TestNotebookEditViewPOST:
    @pytest.fixture(autouse=True)
    def initial(self, client):
        self.notebook = NoteBook.objects.create(title="new book", content="hello world :^)")
        url = reverse("notebooks:edit", kwargs={"pk": self.notebook.id})
        self.response = client.post(url, data={"title": "updated", "content": ":^)"})

    def test_status_code(self):
        asserts.assertRedirects(
            self.response,
            reverse("notebooks:edit", kwargs={"pk": self.notebook.id}),
            status_code=302,
        )

    def test_model_is_updated(self):
        notebook = NoteBook.objects.get(pk=self.notebook.id)
        assert notebook.title == "updated"
        assert notebook.content == ":^)"
