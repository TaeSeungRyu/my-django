from django.http import JsonResponse
from .models import Post

def get_posts(request):
    posts = Post.objects.all().values(
        "id",
        "title",
        "content",
        "created_at"
    )

    return JsonResponse({
        "success": True,
        "data": list(posts)
    })