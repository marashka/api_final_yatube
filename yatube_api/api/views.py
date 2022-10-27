from django.shortcuts import get_object_or_404
from rest_framework import filters, mixins, permissions, viewsets

from posts.models import Group, Post
from .permissions import IsAuthorOrReadOnlyPermission
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class PostGetOnlyViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                         mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    pass


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnlyPermission
    )

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author=author)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (
        permissions.AllowAny,
    )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnlyPermission
    )

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        return post.comments.all()

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(post=post, author=self.request.user)


class FollowViewSet(PostGetOnlyViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=following__username',)

    def get_queryset(self):
        user = self.request.user
        return user.subscriptions.all()

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
