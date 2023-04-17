
from .models import Post
from rest_framework import generics, filters
from rest_framework.permissions import IsAdminUser
from .serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    """
    List posts or create a post as admin
    """
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [
        filters.SearchFilter,
    ]
    search_fields = [
        'title',
    ]


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it
    """
    serializer_class = PostSerializer
    queryset = Post.objects.all()