from django.contrib import admin
from django.urls import path, include
from .views import hello, index

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('', index),
    path('api/board/', include('board.urls')),  #board/urls.py로 전달함!

    # DRF 로그인 및 로그아웃 기능
    path("api-auth/", include("rest_framework.urls")),    


    path("api/token/", TokenObtainPairView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),
    path("api/token/verify/", TokenVerifyView.as_view()),    
]
