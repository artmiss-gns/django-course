from django.urls import path
from . import views

urlpatterns = [
    path("", views.main),
    path('<int:month>/', views.numeric_month_challenge),
    path('<str:month>/', views.month_challenge, name="month_challenges"),
]