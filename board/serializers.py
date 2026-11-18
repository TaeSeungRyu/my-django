from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "content",
            "created_at",
            "view_count",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "view_count",
        ]