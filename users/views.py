from django.shortcuts import render
from .models import User

# View for user profile
def user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'users/profile.html', {'user': user})
