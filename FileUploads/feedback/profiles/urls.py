from django.urls import path

from . import views

urlpatterns = [
    path("", views.CreateProfileView.as_view()),
    path('success_upload', views.SuccessView.as_view()),
    path('all_profiles', views.AllProfiles.as_view()),
]
