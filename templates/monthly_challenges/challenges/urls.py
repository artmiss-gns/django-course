from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_page'),
    path('<int:month>', views.numeric_monthly_challenges, name='numeric_month_challenges'),
    path('<str:month>', views.monthly_challenges, name='month_challenges'),
]