from django.urls import path
from .views import index, PostsView, create_user, return_to_home, create_post, user_information, search_videos

urlpatterns = [
    path("utils/youtube/", search_videos, name="videos"),
    path("check/", index, name='check'),
    path("", return_to_home, name='homepage'),
    path("users/<int:pk>", user_information, name="user_information"),
    path("posts/", PostsView.as_view(), name='posts'),
    path("users/sign-up/", create_user, name="new_user"),
    path("posts/new_post", create_post, name='new_post')
]
