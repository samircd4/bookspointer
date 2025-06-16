from django.conf import settings
from django.db import models

class Book(models.Model):
    book_id = models.CharField(max_length=10,primary_key=True)
    title = models.CharField(max_length=255, unique=True)
    reviewed_by_shraiya = models.BooleanField(default=False)
    author = models.CharField(max_length=255, blank=True, null=True)
    author_id = models.IntegerField()
    category = models.CharField(max_length=255, blank=True, null=True)
    category_id = models.IntegerField()
    is_posted = models.BooleanField(default=False)
    book_link = models.CharField(max_length=500)
    content = models.TextField()  # Stores HTML string

    def __str__(self):
        return self.title


class AppUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Store hashed passwords in production!
    token = models.CharField(max_length=1000, blank=True, null=True)
    has_profile_image = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Author(models.Model):
    IS_SCRAPED = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    
    author_id = models.CharField(max_length=25, primary_key=True)
    author_name = models.CharField(max_length=255)
    author_link = models.CharField(max_length=500)
    is_scraped = models.CharField(max_length=5, choices=IS_SCRAPED, default='no')
    
    def __str__(self):
        return f'{self.author_id}'