from rest_framework import serializers
from .models import Book, AppUser, Category, Author

class BookSerializer(serializers.ModelSerializer):
    category_id = serializers.CharField(source='category_id.category_id', read_only=True)
    class Meta:
        model = Book
        fields = [
            'book_id', 'title', 'reviewed_by_shraiya', 'author', 'author_id',
            'category', 'category_id', 'is_posted', 'book_link', 'content'
        ]


class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'