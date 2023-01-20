from django.urls import path

from pages.views import PagesIndexView, PagesSearchView

app_name = "pages"

urlpatterns = [
    path("", PagesIndexView.as_view(), name="index"),
    path("search/", PagesSearchView.as_view(), name="search"),
]
