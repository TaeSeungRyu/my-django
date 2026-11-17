from django.urls import path
from .views import posts, post_detail, test_page

urlpatterns = [
    path("posts/", posts),
    path("posts/<int:post_id>/", post_detail),
    path("posts/test/", test_page),
]