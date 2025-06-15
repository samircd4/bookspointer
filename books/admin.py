from unfold.admin import ModelAdmin  # use Unfold's ModelAdmin
from .models import Book, AppUser
# from unfold.sites import UnfoldAdminSite
from django.contrib import admin 
from django.utils.html import format_html

class BookAdmin(ModelAdmin):
    list_display = ('book_id', 'title', 'author', 'reviewed_by_shraiya', 'category', 'category_id', 'is_posted', 'book_link_display')
    search_fields = ('title', 'author', 'category')
    list_editable = ('reviewed_by_shraiya','category_id')
    
    # Add column attributes for width
    attrs = {
        "category": {"td": {"style": "min-width: 600px;"}}
    }
    def book_link_display(self, obj):
        return format_html(
            "<a href='{url}' target='_blank' style='background:#9546ddd9;text-align:center;padding:6px;border-radius:5px;font-size:14px'>View Book</a>", url=obj.book_link
        )
    book_link_display.short_description = "Book Link"
    
class AppUserAdmin(ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'password', 'has_profile_image', 'is_verified')
    list_editable = ('has_profile_image',)
    search_fields = ('first_name', 'last_name', 'email')



# class CustomAdminSite(UnfoldAdminSite):
#     site_header = "Sarker Book Admin"
#     site_title = "Sarker Book Admin Portal"
#     index_title = "Welcome to BooksPointer Admin"

# admin_site = CustomAdminSite(name='custom_admin')

# Register your models to the custom site:
admin.site.register(Book, BookAdmin)
admin.site.register(AppUser, AppUserAdmin)