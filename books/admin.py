from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Admin interface for managing Book instances."""

    list_display = ['id', 'title', 'author',
                    'formatted_price', 'genre', 'publication_date']
    list_display_links = ['title']
    search_fields = ['title', 'author']
    list_filter = ['genre', 'publication_date']

    def formatted_price(self, obj):
        """Format the price of the book for display in the admin interface."""
        return f"RM {obj.price:.2f}"

    formatted_price.short_description = 'Price'
