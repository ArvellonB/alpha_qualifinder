from django.shortcuts import render
from .models import Connection

# View for user connections
def user_connections(request, user_id):
    connections = Connection.objects.filter(user1_id=user_id)
    return render(request, 'connections/connections.html', {'connections': connections})
