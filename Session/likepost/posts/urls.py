from django.urls import path
from . import views

urlpatterns = [
    path('', views.Post.as_view(), name='post'),
    path('add_post', views.AddPost.as_view(), name='add-post'),
    path('successful_submit', views.SuccessfulSubmit.as_view(), name='successful-submit'),
]
