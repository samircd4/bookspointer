from django.urls import path, include
# from books.admin import admin_site  # import your custom site
from django.contrib import admin


urlpatterns = [
    path("api/", include("books.urls")),
    path("", admin.site.urls),
]
