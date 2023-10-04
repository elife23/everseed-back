from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
import base64
from cryptography.fernet import Fernet
from .serializers import *
from .models import *

DOMAINS = 'http://'

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


# Generate a Meet Session for a user --
@api_view(['POST'])
def StartMeet(request):
    # Create meeting data model and store it
    serializer = MeetingSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response({"error" : "Wrong data format"}, status = status.HTTP_400_BAD_REQUEST)

    # Current meeting instance
    meeting = Meeting.objects.get(pk = serializer.data['id'])

    # Store meetingId
    value = str(meeting.id)

    # Generate base key
    base = Fernet(Fernet.generate_key())

    # Encrypted value by key
    encrypted_key = base.encrypt(value.encode())
    #decrypted_key = base.decrypt(encrypted_key.decode())
    #encrypted_key = base64.urlsafe_b64encode(key.encode())
    #original_link = base64.urlsafe_b64decode(f_value.decode())

    # Generate complete link for join a meet
    #link = DOMAINS + request.get_host() + '/api/JoinMeet/' + str(encrypted_key) + '/'

    content = {
        "MeetingId" : meeting.id,
        "MeetingLink" : encrypted_key,
    }
    return Response({"success" : content}, status = status.HTTP_200_OK)


# Generate a Meet Session for a user --
@api_view(['POST'])
def SettingMeet(request, id):
    # Check if an instance of Meetingroom already exists
    try:
        meeting_room = Meetingroom.objects.get(meetingid = id)
        serializer = MeetingroomSerializer(instance = meeting_room, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"success" : "Meetingroom update"}, status = status.HTTP_200_OK)
        else:
            return Response({"error" : "Wrong data format"}, status = status.HTTP_400_BAD_REQUEST)
    except ObjectDoesNotExist:
        pass

    # We add meetingid to request.data
    request.data._mutable = True
    request.data['meetingid'] = id

    # We store Meetingroom
    serializer = MeetingroomSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response({"error" : "Wrong data format"}, status = status.HTTP_400_BAD_REQUEST)
    
    return Response({"success" : "Setting Meetingroom added"}, status = status.HTTP_200_OK)



"""
# Join a User Meet -------------------
@api_view(['GET'])
def JoinMeet(request, id):
    
    return Response({"success" : "Join sucessfully"}, status = status.HTTP_200_OK)
"""