from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
    path("", include("pages.urls")),
    path("notebook/", include("notebooks.urls")),
]
