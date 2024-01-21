from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render

from .models import Post
from .serializers import  PostSerilazer


class PostListView(APIView):
    def get(self, request):
        post = Post.objects.all()
        serilizer = PostSerilazer(post,many=True)
        return Response(serilizer.data)