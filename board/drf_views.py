from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Post
from .serializers import PostSerializer

from django.shortcuts import get_object_or_404


@api_view(["GET", "POST"])
def posts(request):

    # 전체 조회
    if request.method == "GET":
        posts = Post.objects.all().order_by("-id")

        serializer = PostSerializer(posts, many=True)

        return Response({
            "data": serializer.data
        })

    # 등록
    if request.method == "POST":
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {"data": serializer.data},
                status=status.HTTP_201_CREATED
            )

        return Response(
            {"errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )




@api_view(["GET", "PUT", "PATCH", "DELETE"])
def post_detail(request, post_id):

    # 게시글 조회 (없으면 404)
    post = get_object_or_404(Post, id=post_id)

    # 상세 조회
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response({"data": serializer.data})

    # 전체 수정
    if request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"data": serializer.data})

    # 부분 수정
    if request.method == "PATCH":
        serializer = PostSerializer(
            post,
            data=request.data,
            partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"data": serializer.data})

    # 삭제
    if request.method == "DELETE":
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    