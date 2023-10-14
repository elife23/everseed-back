from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password, check_password, hashlib
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from drf_yasg.utils import swagger_auto_schema
import base64
from cryptography.fernet import Fernet
from .serializers import *
from .models import *

BASE = Fernet(Fernet.generate_key())

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
def showUser(request, pkUser):
    try:
        user = User.objects.get(id = pkUser)
    except ObjectDoesNotExist:
        return Response({'error': 'Not user at this ID'}, status = status.HTTP_400_BAD_REQUEST)

    serialization = UserSerializer(user)
    return Response(serialization.data)


# Create user ------------------------
@swagger_auto_schema(method='post', request_body=UserSerializer)
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
@swagger_auto_schema(method='post', request_body=MeetingSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def StartMeet(request):
    # Create meeting data model and store it
    serializer = MeetingSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response({"error" : "Wrong data format"}, status = status.HTTP_400_BAD_REQUEST)

    # Format meeting id in string
    value = str(serializer.data['id'])

    # Generate safe code
    code = base64.urlsafe_b64encode(value.encode())

    # Response headers
    content = {
        "MeetingId" : serializer.data['id'],
        "MeetingLink" : code,
    }
    return Response({"success" : content}, status = status.HTTP_200_OK)


# Generate a Meet Session for a user --
@swagger_auto_schema(method='post', request_body=MeetingroomSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def SettingMeet(request):
    # Check if an instance of Meetingroom already exists
    try:
        meeting_room = Meetingroom.objects.get(meetingid = request.data['meetingid'])
        serializer = MeetingroomSerializer(instance = meeting_room, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"success" : "Meetingroom update"}, status = status.HTTP_200_OK)
        else:
            return Response({"error" : "Wrong data format"}, status = status.HTTP_400_BAD_REQUEST)
    except ObjectDoesNotExist:
        pass

    # We store Meetingroom
    serializer = MeetingroomSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response({"error" : "Wrong data format"}, status = status.HTTP_400_BAD_REQUEST)
    
    return Response({"success" : "Setting Meetingroom added"}, status = status.HTTP_200_OK)



# Join a User Meet -------------------
@swagger_auto_schema(method='post', request_body=ParticipantSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def JoinMeet(request):
    # For format data sended 
    request.data._mutable = True

    # Decode meeting code and parse user id in int and try meeting code validity 
    try:
        request.data['meetingid'] = int( base64.urlsafe_b64decode(request.data['meetingid']) ) 
        request.data['userid'] = int( request.data['userid'] )

        # We verify that user doesn't already join this meeting
        try:
            participant = Participant.objects.get(userid = request.data['userid'])
            return Response({"success" : "You have already joined this meeting"}, status = status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            pass

        # We verify that user try to join a valid meeting
        try:
            meeting = Meeting.objects.get(id = request.data['meetingid'], deleted = 0)

            # Serialize it
            serializer = ParticipantSerializer(data = request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({"success" : "You going to join the meeting"}, status = status.HTTP_200_OK)
            else:
                return Response({"error" : "Wrong format data"}, status = status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({"error" : "Meeting finised or doen't exists"}, status = status.HTTP_400_BAD_REQUEST)
    except:
        return Response({"error" : "Invalid format meeting code."}, status = status.HTTP_400_BAD_REQUEST)