from django.shortcuts import render
from .models import Book
# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(
        request, 'book_outlet/index.html', {'books': books}
    )

def book(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(
        request, 'book_outlet/book.html', {'book': book}
    )