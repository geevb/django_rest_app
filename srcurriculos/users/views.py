from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

import requests

from srcurriculos.users.serializers import CreateUserSerializer

CLIENT_ID = 'xAP80lbdRZbMBUn7jYDLYPpKPHMhNGF1eg1rEk8i'
CLIENT_SECRET = 'ZbxBHMd7lxdONU8ijMkcb0Xt4kbl7g2qh9XfGOAwQXmJkbzZ5rKYhoyZ5koay8yLfKJOjOLyknprBqU2Hhv32GdX6Rv4E3oDZ7nSd7tUMIRyMX1jGPLWQLLTQIqrD8M7'

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = CreateUserSerializer(data=request.data) 
    if serializer.is_valid():

        serializer.save()
        r = requests.post('http://127.0.0.1:8000/o/token/',
            data = {
                'grant_type': 'password',
                'username': request.data['username'],
                'password': request.data['password'],
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            }
        )
        return JsonResponse({'response': str(r.json())}, status = 201)
    return JsonResponse({'response': str(serializer.errors)}, status = 400)
