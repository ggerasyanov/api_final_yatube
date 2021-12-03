from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('posts', views.PostViewSet)
router.register('groups', views.GroupViewSet)
router.register('follow', views.FollowViewSet, basename='follow')
router.register(r'posts/(?P<post_id>\d+)/comments',
                views.CommentViewSet, basename='comment')

urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls))
]
