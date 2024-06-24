from django.urls import path
from .views import review, ThankYou

urlpatterns = [
    path('', review.as_view()),
    path('thank_you', ThankYou.as_view(), name='thank_you_page')
]
