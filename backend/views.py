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
import secrets
from cryptography.fernet import Fernet
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
def ViewUser(request, pkUser):
    try:
        user = User.objects.get(id = pkUser)
    except ObjectDoesNotExist:
        return Response({'error': 'Not user at this ID'}, status = status.HTTP_400_BAD_REQUEST)

    serialization = UserSerializer(user)
    return Response({"response" : serialization.data}, status = status.HTTP_200_OK)


# Create user ------------------------
@swagger_auto_schema(method='post', request_body=UserSerializer)
@api_view(['POST'])
def SignUp(request):
    try:
        # Save temporary current user password for make comparizon
        temp_password = request.data['password']

        # Hashing current user password
        request.data['password'] = make_password(request.data['password'])
    except KeyError:
        temp_password = ''

    # Insert data user
    serializer = UserSerializer(data = request.data) 

    if serializer.is_valid():
        # We get all user
        all_user = User.objects.all();

        for user in all_user:
            # We compare each user password with current user password
            is_exists_password = check_password(temp_password, user.password)

            if is_exists_password == True:
                return Response({"error" : "Password is not secured"}, status = status.HTTP_400_BAD_REQUEST)
            else:
                pass
    
        serializer.save()
        return Response({"success" : "User registered with success"}, status = status.HTTP_201_CREATED)
    # Sinon
    return Response({"error" : "Wrong data format or firstname is already used"}, status = status.HTTP_400_BAD_REQUEST)    


# Launch a Meeting Session -----------
@swagger_auto_schema(method='post', request_body=MeetingSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def LaunchMeeting(request):
    # Create meeting data model and store it
    serializer = MeetingSerializer(data = request.data)

    if serializer.is_valid():
        # We save meeting
        serializer.save()

        return Response({"success" : "Meeting Launched"}, status = status.HTTP_200_OK)
    else:
        return Response({"error" : "Wrong data format"}, status = status.HTTP_400_BAD_REQUEST)



# Custom a MeetingRoom of user -------------
@swagger_auto_schema(method='post', request_body=MeetingroomSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def SettingMeeting(request, roomName):
    try:
        # We get roomName of current meeting 
        meeting = Meeting.objects.get(roomname = roomName)

        # We cast field meeting id with current meeting id
        request.data['meetingid'] = meeting.id

        try:  
            # Check if an instance of Meetingroom already exists
            meeting_room = Meetingroom.objects.get(meetingid = request.data['meetingid'])

            # We update MeetingRoom
            serializer = MeetingroomSerializer(instance = meeting_room, data = request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({"success" : "Meetingroom update"}, status = status.HTTP_200_OK)
            else:
                return Response({"error" : "Wrong data format"}, status = status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            pass

        # We insert Meetingroom
        serializer = MeetingroomSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"success" : "Meetingroom inserted"}, status = status.HTTP_200_OK)
        else:
            return Response({"error" : "Wrong data format"}, status = status.HTTP_400_BAD_REQUEST)
    except ObjectDoesNotExist:
        return Response({"error" : "Invalid meeting code"}, status = status.HTTP_400_BAD_REQUEST)


# Join a Meeting --------------------
@swagger_auto_schema(method='post', request_body=ParticipantSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def JoinMeeting(request, roomName):
    # We check that user doesn't already join this meeting
    try:
        participant = Participant.objects.get(userid = request.data['userid'])
        return Response({"success" : "You have already joined this meeting"}, status = status.HTTP_400_BAD_REQUEST)
    except ObjectDoesNotExist:
        pass

    # We Check if roomName is valid
    try:
        # We get roomName of current meeting 
        meeting = Meeting.objects.get(roomname = roomName)

        # We cast field meeting id with current meeting id
        request.data['meetingid'] = meeting.id

        # We verify that user try to join a valid meeting
        try:
            # We get curent meeting
            meeting = Meeting.objects.get(id = request.data['meetingid'], deleted = 0)

            # We get participant size
            size_participant = Participant.objects.filter(meetingid = meeting.id).count()
            print(size_participant)

            # We get maxCapacity of meetingroom
            meetingroom = Meetingroom.objects.get(meetingid = meeting.id)

            # We Check that participant size is not greater than maxCapacity
            try:
                assert size_participant > meetingroom.maxcapacity

                # Create Data participant
                serializer = ParticipantSerializer(data = request.data)

                if serializer.is_valid():
                    serializer.save()
                    return Response({"success" : "You going to join the meeting"}, status = status.HTTP_200_OK)
                else:
                    return Response({"error" : "Wrong format data"}, status = status.HTTP_400_BAD_REQUEST)
            except AssertionError:
                return Response({"error" : "Meeting is complete"}, status = status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({"error" : "Meeting doen't exists"}, status = status.HTTP_400_BAD_REQUEST)
    except ObjectDoesNotExist:
        return Response({"error" : "Invalid Meeting code"}, status = status.HTTP_400_BAD_REQUEST)


# Add comment of meeting -------------
@swagger_auto_schema(method='put', request_body=CommentmeetingSerializer)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def AddCommentMeeting(request, pkUser, roomName):
    # Check if roomName is valid
    try:
        # We get roomName of current meeting 
        meeting = Meeting.objects.get(roomname = roomName)

        # We cast field meeting id with current meeting id
        request.data['meetingid'] = meeting.id

        # We verify validity of meeting
        try:
            meeting = Meeting.objects.get(id = request.data['meetingid'])
        except:
            return Response({"error" : "Meeting doen't exists"}, status = status.HTTP_400_BAD_REQUEST)
        
        # We verify if he is participant of the meeting
        try:
            participant = Participant.objects.get(userid = pkUser)

            # Create Commentmeeting data model and store it
            serializer = CommentmeetingSerializer(data = request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({"success" : "Comment added with success"}, status = status.HTTP_200_OK)
            else:
                return Response({"error" : "Wrong format data"}, status = status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({"error" : "He must be participant for send comment"}, status = status.HTTP_400_BAD_REQUEST)
    except ObjectDoesNotExist:
        return Response({"error" : "Invalid Meeting code"}, status = status.HTTP_400_BAD_REQUEST)



# Display Comment of meeting ---------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ViewCommentMeeting(request, roomName):
    # Check if meeting is valid
    try:
        meeting = Meeting.objects.get(roomname = roomName)

        # Get all comments of meeting
        commentmeeting = Commentmeeting.objects.all().filter(meetingid = meeting.id)

        # We convert data in valid format
        serialization = CommentmeetingSerializer(commentmeeting, many = True)

        return Response({"response" : serialization.data}, status = status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({"error" : "None comments found for this meeting"}, status = status.HTTP_400_BAD_REQUEST)



# Launch a Whiteboard  -----------------
@swagger_auto_schema(method='post', request_body=WhiteboardSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def LaunchWhiteboard(request):
    # Create whiteboard data model and store it
    serializer = WhiteboardSerializer(data = request.data)

    if serializer.is_valid():
        # We save whiteboard
        serializer.save()

        return Response({"success" : "Whiteboard Launched"}, status = status.HTTP_200_OK)
    else:
        return Response({"error" : "Wrong data format"}, status = status.HTTP_400_BAD_REQUEST)


"""
# Launch a Whiteboard  -----------------
@swagger_auto_schema(method='put', request_body=WhiteboardSerializer)
@api_view(['put'])
@permission_classes([IsAuthenticated])
def AddCommentWhiteboard(request, whitename):
    # Create whiteboard data model and store it
    serializer = WhiteboardSerializer(data = request.data)

    if serializer.is_valid():
        # We save whiteboard
        serializer.save()

        return Response({"success" : "Whiteboard Launched"}, status = status.HTTP_200_OK)
    else:
        return Response({"error" : "Wrong data format"}, status = status.HTTP_400_BAD_REQUEST)
"""