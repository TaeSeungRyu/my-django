from django.urls import path
from .views import posts, post_detail, test_page
#from . import drf_views
from .drf_views import posts as drf_posts

urlpatterns = [
    path("posts/", posts),
    path("posts/<int:post_id>/", post_detail),
    path("posts/test/", test_page),
    # DRF API
    path("drf/posts/", drf_posts),    
]