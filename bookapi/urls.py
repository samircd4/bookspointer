from django.urls import path, include
# from books.admin import admin_site  # import your custom site
from django.contrib import admin


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("books.urls")),
]
