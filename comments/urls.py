from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:post_id>/', views.post_comments, name='post_comments'),
]
