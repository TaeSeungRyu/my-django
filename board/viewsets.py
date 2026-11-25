from rest_framework import viewsets
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
)

from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all().order_by("-id")
    serializer_class = PostSerializer

    def get_permissions(self):
        print("my permission : ",self.action)

        # 전체 조회, 상세 조회
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]

        # 등록, 전체 수정, 부분 수정
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated()]

        # 삭제
        if self.action == "destroy":
            return [IsAdminUser()]

        # 그 외 요청
        return [IsAuthenticated()]
# 기본 URL 생성 모습
# 전체 조회	GET	/api/board/viewset/posts/
# 상세 조회	GET	/api/board/viewset/posts/1/
# 등록	POST	/api/board/viewset/posts/
# 전체 수정	PUT	/api/board/viewset/posts/1/
# 부분 수정	PATCH	/api/board/viewset/posts/1/
# 삭제	DELETE	/api/board/viewset/posts/1/