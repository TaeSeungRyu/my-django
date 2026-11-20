from django.urls import path
from .views import posts, post_detail, test_page
#from . import drf_views
from .drf_views import (
    posts as drf_posts,
    post_detail as drf_post_detail,
)
from .api_views import PostListView, PostDetailView


urlpatterns = [
    path("posts/", posts),
    path("posts/<int:post_id>/", post_detail),
    path("posts/test/", test_page),
    # DRF API
    path("drf/posts/", drf_posts),
    path("drf/posts/<int:post_id>/", drf_post_detail),

    # DRF APIView
    path("apiview/posts/", PostListView.as_view()),
    path("apiview/posts/<int:post_id>/", PostDetailView.as_view()),    
]