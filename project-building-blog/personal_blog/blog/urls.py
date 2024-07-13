from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('blogs', views.all_blogs, name='all_blogs'),
    path('blogs/read_later', views.ReadLaterView.as_view(), name='read_later'),
    path('blogs/save_for_later/<slug:slug>', views.SaveForLaterView.as_view(), name='save_for_later'),
    path('blogs/<slug:slug>/add_comment', views.AddCommentView.as_view(), name='add_comment'),
    path('blogs/<slug:slug>', views.single_blog, name='single_blog'),
]
