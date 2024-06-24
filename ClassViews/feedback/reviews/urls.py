from django.urls import path
from .views import review, thank_you

urlpatterns = [
    path('', review.as_view()),
    path('thank_you', thank_you,)
]
