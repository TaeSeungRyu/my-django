from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import PostSerializer
from .models import Post


class PostListView(APIView):

    # GET /posts/
    def get(self, request):
        posts = Post.objects.all().order_by("-id")
        serializer = PostSerializer(posts, many=True)

        return Response({
            "data": serializer.data
        })

    # POST /posts/
    def post(self, request):
        serializer = PostSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"data": serializer.data},
            status=status.HTTP_201_CREATED
        )

class PostDetailView(APIView):

    # GET /posts/1/
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        serializer = PostSerializer(post)

        return Response({"data": serializer.data})

    # PUT /posts/1/
    def put(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)

        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"data": serializer.data})

    # PATCH /posts/1/
    def patch(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)

        serializer = PostSerializer(
            post,
            data=request.data,
            partial=True
        )

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"data": serializer.data})

    # DELETE /posts/1/
    def delete(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)