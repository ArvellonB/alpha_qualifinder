from django.shortcuts import render
from .models import Comment

# View for displaying comments on a post
def post_comments(request, post_id):
    comments = Comment.objects.filter(post_id=post_id)
    return render(request, 'comments/comments.html', {'comments': comments})
