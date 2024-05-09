from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# View for displaying posts by user
def user_posts(request, user_id):
    posts = Post.objects.filter(user_id=user_id)
    return render(request, 'posts/posts.html', {'posts': posts})

def create_post(request, user_id):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user_id = user_id  # Set the user ID to the logged-in user's ID
            new_post.save()
            return redirect('some-view-to-redirect')  # Redirect to another view after posting
    else:
        form = PostForm()
    return render(request, 'posts/create_post.html', {'form': form})
