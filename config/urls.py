from django.contrib import admin
from django.urls import path
from .views import hello, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('', index),
]
