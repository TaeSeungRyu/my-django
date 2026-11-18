from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Post
from .serializers import PostSerializer


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