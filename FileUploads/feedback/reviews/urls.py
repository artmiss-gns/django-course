from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
     path("", views.ReviewView.as_view()),
     path("thank-you", views.ThankYouView.as_view()),
     path("reviews", views.ReviewsListView.as_view()),
     path("reviews/<int:pk>", views.SingleReviewView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
