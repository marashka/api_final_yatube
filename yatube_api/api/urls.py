from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_ap_v1 = DefaultRouter()
router_ap_v1.register(r'v1/posts', PostViewSet, basename='post')
router_ap_v1.register(r'v1/groups', GroupViewSet, basename='group')
router_ap_v1.register(
    r'v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='comment'
)
router_ap_v1.register(r'v1/follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('', include(router_ap_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
