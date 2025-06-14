from django.urls import path, include
from books.admin import admin_site  # import your custom site


urlpatterns = [
    path("admin/", admin_site.urls),
    path("api/", include("books.urls")),
]
