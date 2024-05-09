from django.urls import path
from . import views

urlpatterns = [
    path('user/<int:user_id>/', views.user_connections, name='user_connections'),
]
