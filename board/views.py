import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Post
from django.shortcuts import render



def post_to_dict(post):
    return {
        "id": post.id,
        "title": post.title,
        "content": post.content,
        "view_count": post.view_count,
        "created_at": post.created_at.isoformat(),
    }


@csrf_exempt  # 학습용: 운영 환경에서는 인증 및 CSRF 보호 필요
def posts(request):

    # 전체 조회
    if request.method == "GET":
        data = [
            post_to_dict(post)
            for post in Post.objects.all().order_by("-id")
        ]
        return JsonResponse({"data": data})

    # 등록
    if request.method == "POST":
        try:
            body = json.loads(request.body)
        except (ValueError, UnicodeDecodeError):
            return JsonResponse({"error": "잘못된 JSON"}, status=400)

        if not isinstance(body, dict):
            return JsonResponse({"error": "JSON 객체가 필요합니다."}, status=400)

        title = body.get("title")
        content = body.get("content")

        if not isinstance(title, str) or not title.strip() or len(title) > 200:
            return JsonResponse({"error": "제목을 확인하세요."}, status=400)

        if not isinstance(content, str):
            return JsonResponse({"error": "내용을 확인하세요."}, status=400)

        post = Post.objects.create(
            title=title,
            content=content,
        )

        return JsonResponse(
            {"data": post_to_dict(post)},
            status=201
        )

    return JsonResponse({"error": "허용되지 않는 메서드"}, status=405)


@csrf_exempt  # 학습용으로만 사용
def post_detail(request, post_id):

    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return JsonResponse({"error": "게시글 없음"}, status=404)

    # 상세 조회
    if request.method == "GET":
        return JsonResponse({"data": post_to_dict(post)})

    # 수정
    if request.method == "PUT":
        try:
            body = json.loads(request.body)
        except (ValueError, UnicodeDecodeError):
            return JsonResponse({"error": "잘못된 JSON"}, status=400)

        if not isinstance(body, dict):
            return JsonResponse({"error": "JSON 객체가 필요합니다."}, status=400)

        title = body.get("title")
        content = body.get("content")

        if not isinstance(title, str) or not title.strip() or len(title) > 200:
            return JsonResponse({"error": "제목을 확인하세요."}, status=400)

        if not isinstance(content, str):
            return JsonResponse({"error": "내용을 확인하세요."}, status=400)

        post.title = title
        post.content = content
        post.save()

        return JsonResponse({"data": post_to_dict(post)})

    # 삭제
    if request.method == "DELETE":
        post.delete()
        return JsonResponse({"success": True})

    return JsonResponse({"error": "허용되지 않는 메서드"}, status=405)


#페이지 생성 샘플
def test_page(request):
    return render(request, "board/test.html")