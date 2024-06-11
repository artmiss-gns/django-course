from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main_page'),
    path('<slug:book_id>', views.book, name='book_page')
]