from django.contrib import admin
from .models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    empty_value_display = "---"
    list_display = ('title', 'author', 'is_bestseller', 'rating')  # columns to display in the list view
    list_filter = ('is_bestseller', 'rating', 'author')  # filters in the right sidebar
    search_fields = ('title', 'author')  # searchable fields
    ordering = ('title',)  # default ordering
    # readonly_fields = ('slug',)  # read-only fields
    prepopulated_fields = {'slug': ('title',)}
    # fieldsets = (
    #     (None, {'fields': ('title', 'author', 'is_bestseller', 'rating')}),
    #     ('Advanced options', {'fields': ('slug',)}),
    # )  # fieldsets in the edit view


admin.site.register(Book, BookAdmin)