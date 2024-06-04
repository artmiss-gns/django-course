from django.urls import path
from . import views

urlpatterns = [
    path('', views.challenges_index),
    path('<int:month>', views.numeric_monthly_challenges, name='numeric_month_challenges'),
    path('<str:month>', views.monthly_challenges, name='month_challenges'),
]