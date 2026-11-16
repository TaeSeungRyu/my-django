from django.contrib import admin
from django.urls import path, include
from .views import hello, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('', index),
    path('api/board/', include('board.urls')),  #board/urls.py로 전달함!
]
