from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import *
from .models import *


# Custom Token system : Login user --
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.firstname
        token['password'] = user.password
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# Show user's informations ----------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def showUser(request, id):
    try:
        user = User.objects.get(id = id)
    except ObjectDoesNotExist:
        return Response({'error': 'Not user at this ID'}, status = status.HTTP_400_BAD_REQUEST)

    serialization = UserSerializer(user)
    return Response(serialization.data)


# Create user ------------------------
@api_view(['POST'])
def SignUp(request):
    # Save user password
    try:
        temp_password = request.data['password']
        request.data['password'] = make_password(request.data['password'])
    except KeyError:
        temp_password = ''

    # Create data user model
    serializer = UserSerializer(data = request.data) 

    # Si le format de données est valide
    if serializer.is_valid():
        # On verifie que l'intégrité du password est respecté
        all_user = User.objects.all();
        for user in all_user:
            verify = check_password(temp_password, user.password)
            if verify == True:
                user_exists_error = {"error" : "password is not secured"}
                return Response(user_exists_error, status = status.HTTP_400_BAD_REQUEST)
            else:
                pass
    
        serializer.save()
        return Response({"success" : "user created !"}, status = status.HTTP_201_CREATED)
    # Sinon
    print(serializer.errors)
    return Response({"error" : "Wrong data format, or firstname is not good"}, status = status.HTTP_400_BAD_REQUEST)    

