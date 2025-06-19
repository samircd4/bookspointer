from rest_framework import viewsets
from .models import Book, AppUser, Category
from .serializers import BookSerializer, AppUserSerializer, CategorySerializer
from django.http import HttpResponse




def index(request):
    return HttpResponse("<h2>Welcome to BooksPointer Dashboard!</h2><h4>Go to <a href='https://bookspointer.onrender.com/admin'>Dashboard</a> ", content_type="text/html")


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AppUserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer