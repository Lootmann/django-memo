import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from pytest_django import asserts


@pytest.mark.django_db
class TestAccountsSignup:
    @pytest.fixture(autouse=True)
    def initial(self, client):
        credential = {
            "username": "hoge",
            "email": "hoge@email.com",
            "password1": "hogehoge123",
            "password2": "hogehoge123",
        }
        self.url = reverse("accounts:signup")
        self.response = client.post(self.url, credential)

    def test_model_is_created(self):
        users = get_user_model().objects.all()
        assert users.count() == 1
        assert users.first().username == "hoge"
        assert users.first().email == "hoge@email.com"
        assert users.first().is_active is True
        assert users.first().is_staff is False
        assert users.first().is_superuser is False


@pytest.mark.django_db
class TestAccountsLogin:
    @pytest.fixture(autouse=True)
    def initial(self, client):
        credential = {
            "username": "testman",
            "email": "testman@email.com",
            "password": "testman@123",
        }
        get_user_model().objects.create_user(**credential)

        self.url = reverse("login")
        self.response = client.post(
            self.url,
            {"username": credential["username"], "password": credential["password"]},
        )

    def test_status_code(self):
        asserts.assertRedirects(self.response, reverse("pages:index"), status_code=302)
