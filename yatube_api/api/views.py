from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from . import serializers
from .permissions import AuthorOrReadOnly
from posts.models import Group, Post, User


class PostViewSet(viewsets.ModelViewSet):
    """Вьюстер для работы с моделью Post."""
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = (AuthorOrReadOnly, )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюстер для работы с моделью Group."""
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюстер для работы с моделью Comment."""
    serializer_class = serializers.CommentSerializer
    permission_classes = (AuthorOrReadOnly, )

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        return post.comments.all()

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post_obj = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post_obj)


class FollowViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """Mixins для работы с моделью Follow."""
    serializer_class = serializers.FollowSerializer
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('following__username', 'user__username')

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        return user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
