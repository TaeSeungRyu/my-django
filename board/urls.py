from django.urls import path
from .views import posts, post_detail, test_page
#from . import drf_views
from .drf_views import (
    posts as drf_posts,
    post_detail as drf_post_detail,
)
from .api_views import PostListView, PostDetailView

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import PostViewSet

router = DefaultRouter()
router.register("posts", PostViewSet, basename="posts")  # URL 경로, 뷰셋, 내부에서 관리하는 name

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

    # DRF ModelViewSet
    path("viewset/", include(router.urls)),  # viewset/ + posts/ ===> 이렇게 조합이 된다!
]