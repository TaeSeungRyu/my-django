from rest_framework import viewsets

from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet): # CRUD 기능을 상속받음

    queryset = Post.objects.all().order_by("-id") # 어떤 DB 데이터를 사용할지 지정

    serializer_class = PostSerializer # 어떤 Serializer를 사용할지 지정
    
# 기본 URL 생성 모습
# 전체 조회	GET	/api/board/viewset/posts/
# 상세 조회	GET	/api/board/viewset/posts/1/
# 등록	POST	/api/board/viewset/posts/
# 전체 수정	PUT	/api/board/viewset/posts/1/
# 부분 수정	PATCH	/api/board/viewset/posts/1/
# 삭제	DELETE	/api/board/viewset/posts/1/