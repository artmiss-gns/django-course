from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main_page'),
    path('<slug:slug>', views.book, name='book_page')
]