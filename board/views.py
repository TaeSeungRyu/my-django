from django.http import JsonResponse

def get_posts(request):
    posts = [
        {"id": 1, "title": "첫 번째 게시글"},
        {"id": 2, "title": "두 번째 게시글"},
        {"id": 3, "title": "세 번째 게시글"},
    ]

    return JsonResponse({
        "success": True,
        "data": posts
    })