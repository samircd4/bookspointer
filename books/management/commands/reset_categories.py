from django.core.management.base import BaseCommand
from books.models import Category
from django.db import connection


class Command(BaseCommand):
    help = 'Delete all categories and reset the auto-incrementing ID for Category model (SQLite only)'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Deleting all categories...'))
        Category.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('All categories deleted.'))
        self.stdout.write(self.style.WARNING(
            'Resetting auto-increment sequence for Category...'))
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM sqlite_sequence WHERE name='books_category';")
        self.stdout.write(self.style.SUCCESS(
            'Auto-increment sequence reset. Next category will have id=1.'))
