from django.contrib import admin
from .models import Book, Author, Address, Country
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    empty_value_display = "---"
    list_display = ('title', 'author', 'is_bestseller', 'rating')  # columns to display in the list view
    list_filter = ('is_bestseller', 'rating', 'author')  # filters in the right sidebar
    search_fields = ('title', 'author')  # searchable fields
    ordering = ('title',)  # default ordering
    prepopulated_fields = {'slug': ('title',)}

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('FirstName', 'LastName', 'address')

class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'postal_code', 'city')
    
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Country, CountryAdmin)
