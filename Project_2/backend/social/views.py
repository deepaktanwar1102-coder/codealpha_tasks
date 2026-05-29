from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Post, User, Comment, Like, Follow
import json


def get_posts(request):
    posts = []

    for post in Post.objects.all().order_by('-created_at'):
        posts.append({
            "id": post.id,
            "user": post.user.name,
            "text": post.text,
            "time": post.created_at.strftime("%d %b %Y")
        })

    return JsonResponse(posts, safe=False)


@csrf_exempt
def create_post(request):
    if request.method == "POST":

        data = json.loads(request.body)

        user = User.objects.first()

        post = Post.objects.create(
            user=user,
            text=data["text"]
        )

        return JsonResponse({
            "message": "Post Created"
        })
        
@csrf_exempt
def create_comment(request):

    if request.method == "POST":

        data = json.loads(request.body)

        user = User.objects.first()
        post = Post.objects.get(id=data["post_id"])

        Comment.objects.create(
            user=user,
            post=post,
            text=data["text"]
        )

        return JsonResponse({
            "message": "Comment Added"
        })
        
@csrf_exempt
def toggle_like(request):

    if request.method == "POST":

        data = json.loads(request.body)

        user = User.objects.first()
        post = Post.objects.get(id=data["post_id"])

        existing = Like.objects.filter(
            user=user,
            post=post
        )

        if existing.exists():
            existing.delete()
            liked = False
        else:
            Like.objects.create(
                user=user,
                post=post
            )
            liked = True

        return JsonResponse({
            "liked": liked
        })
        
@csrf_exempt
def toggle_follow(request):

    if request.method == "POST":

        data = json.loads(request.body)

        follower = User.objects.first()

        following = User.objects.get(
            id=data["user_id"]
        )

        existing = Follow.objects.filter(
            follower=follower,
            following=following
        )

        if existing.exists():
            existing.delete()

            return JsonResponse({
                "following": False
            })

        Follow.objects.create(
            follower=follower,
            following=following
        )

        return JsonResponse({
            "following": True
        })