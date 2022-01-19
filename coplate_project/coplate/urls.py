from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path(
        "reviews/<int:review_id>",
        views.ReviewDetailView.as_view(), 
        name="review-detail"
    ),
]