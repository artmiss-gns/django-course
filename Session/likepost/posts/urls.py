from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.Post.as_view(), name='post'),
    path('add_post', views.AddPost.as_view(), name='add-post'),
    path('successful_submit', views.SuccessfulSubmit.as_view(), name='successful-submit'),
    path('like_post', views.LikePost.as_view(), name='like-post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
