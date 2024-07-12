from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('blogs', views.all_blogs, name='all_blogs'),
    path('blogs/<slug:slug>/add_comment', views.AddCommentView.as_view(), name='add_comment'),
    path('blogs/<slug:slug>', views.single_blog, name='single_blog'),
]
