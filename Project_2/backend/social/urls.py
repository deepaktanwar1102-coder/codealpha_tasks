from django.urls import path
from .views import get_posts, create_post
from .views import get_posts, create_post, create_comment, toggle_like, toggle_follow

urlpatterns = [
    path('posts/', get_posts),
    path('create-post/', create_post),
    path('create-comment/', create_comment),
    path('toggle-like/', toggle_like),
    path('toggle-follow/', toggle_follow),
]

