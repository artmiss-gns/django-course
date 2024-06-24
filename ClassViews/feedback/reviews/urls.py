from django.urls import path
from .views import review, ThankYou, ListReviews

urlpatterns = [
    path('', review.as_view()),
    path('thank_you', ThankYou.as_view(), name='thank_you_page'),
    path('list_reviews', ListReviews.as_view()),
]
