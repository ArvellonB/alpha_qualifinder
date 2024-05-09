from django.shortcuts import render
from .models import Post

# View for displaying posts by user
def user_posts(request, user_id):
    posts = Post.objects.filter(user_id=user_id)
    return render(request, 'posts/posts.html', {'posts': posts})
