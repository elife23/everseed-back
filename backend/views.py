from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status, exceptions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from drf_yasg.utils import swagger_auto_schema
from cryptography.fernet import Fernet
#import socketio
from .serializers import *
from .models import *

"""
# Define async mode
async_mode = 'eventlet';

# Define socket.io side 
sio = socketio.Server(async_mode=async_mode);
"""

# Login User View  -----------
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # We get email and password in request
        connexion_param = {
            self.username_field: attrs[self.username_field],
            "password": attrs["password"],
        }

        # We check if email exists
        try:
            self.user = User.objects.get(email = connexion_param['email'])
        except ObjectDoesNotExist:
            self.error_messages['no_email'] = _("L'email n'existe pas")
            raise exceptions.NotFound(self.error_messages['no_email'], 'no_email')

        # Try get user data
        user = UserSerializer(self.user)

        # We check password of email
        if not check_password(connexion_param['password'], user.data['password']) == True:
            self.error_messages['no_correspond'] = _("Le mot de passe ne correspond pas")
            raise exceptions.AuthenticationFailed(self.error_messages['no_correspond'], 'no_correspond')

        # Custom token value
        token = self.get_token(self.user)

        # Formatted user data 
        user_data = "{}-{}-{}-{}-{}".format(user.data["id"], user.data["firstname"], user.data["lastname"], user.data["email"], user.data["deleted"]) 

        # Generate hashing key
        key = b'lLRhdzGJTjMiaUH5YcQipAutXu3xRIduEaf04lQAj_c=' #Fernet.generate_key()

        base = Fernet(key)

        # Encode user data
        encoded_user_data = base.encrypt(user_data.encode())

        # Set validate field
        data = super().validate(attrs)

        # Custom validate field
        data["token"] = str(token.access_token) # Add a custom access field
        data["user"] = encoded_user_data
        data.pop('refresh', None) # Remove refresh field
        data.pop('access', None) # Remove default access field

        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Custom value of token
        token['username'] = user.email
        token['password'] = user.password

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

"""
# Show user informations ------------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ViewUser(request, pkUser):
    # Check if user exists
    try:
        user = User.objects.get(id = pkUser)
    except ObjectDoesNotExist:
        return Response({"error": "User not found"}, status = status.HTTP_404_NOT_FOUND)

    serialization = UserSerializer(user)
    return Response({"response" : serialization.data}, status = status.HTTP_200_OK)
"""

# Create user ------------------------
@swagger_auto_schema(method='post', request_body=UserSerializer)
@api_view(['POST'])
def SignUp(request):
    # Hash password
    request.data['password'] = make_password(request.data['password'])

    # Create User data model
    serializer = UserSerializer(data = request.data) 

    if serializer.is_valid():
        serializer.save()

        return Response({"success" : "Utilisateur enregistré"}, status = status.HTTP_201_CREATED)

    # We check if email already exists  
    if serializer.validate_email(serializer.data['email']):
        pass

    # Sinon
    return Response({"error" : "Format de données invalide"}, status = status.HTTP_400_BAD_REQUEST)


# Launch a Meeting Session -----------
@swagger_auto_schema(method='post', request_body=MeetingSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def LaunchMeeting(request):
    # Create meeting data model
    serializer = MeetingSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

        return Response({"success" : "Meeting démarré"}, status = status.HTTP_200_OK)

    return Response({"error" : "Format de données invalide"}, status = status.HTTP_400_BAD_REQUEST)



# Custom MeetingRoom of user -----------
@swagger_auto_schema(method='post', request_body=MeetingroomSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def SettingMeeting(request, roomName):
    try:
        # We get roomName of current meeting 
        meeting = Meeting.objects.get(roomname = roomName)

        # We cast field meetingid with current meeting.id
        request.data['meetingid'] = meeting.id

        try:  
            # Check if an instance of Meetingroom already exists
            meetingRoom = Meetingroom.objects.get(meetingid = request.data['meetingid'])

            # We update MeetingRoom
            serializer = MeetingroomSerializer(instance = meetingRoom, data = request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({"success" : "Meetingroom mis à jour"}, status = status.HTTP_200_OK)
            else:
                return Response({"error" : "Format de données invalide"}, status = status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            pass

        # We insert Meetingroom
        serializer = MeetingroomSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"success" : "Meetingroom configuré"}, status = status.HTTP_201_CREATED)
        else:
            return Response({"error" : "Format de données invalide"}, status = status.HTTP_400_BAD_REQUEST)
    except ObjectDoesNotExist:
        return Response({"error" : "Code de réunion invalide"}, status = status.HTTP_404_NOT_FOUND)


# Join a Meeting --------------------
@swagger_auto_schema(method='post', request_body=ParticipantSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def JoinMeeting(request, roomName):
    # We check that user doesn't already join this meeting
    try:
        participant = Participant.objects.get(userid = request.data['userid'])
        return Response({"error" : "Vous avez déjà rejoint cette réunion"}, status = status.HTTP_400_BAD_REQUEST)
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

            # We get maxCapacity of meetingroom
            meetingroom = Meetingroom.objects.get(meetingid = meeting.id)

            # We Check that participant size is not greater than maxCapacity
            try:
                assert size_participant > meetingroom.maxcapacity

                # Create Data participant
                serializer = ParticipantSerializer(data = request.data)

                if serializer.is_valid():
                    serializer.save()
                    return Response({"success" : "Vous venez de rejoindre la réunion"}, status = status.HTTP_200_OK)
                else:
                    return Response({"error" : "Format de données invalide"}, status = status.HTTP_400_BAD_REQUEST)
            except AssertionError:
                return Response({"error" : "Meeting est complet"}, status = status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({"error" : "Meeting n'existe pas"}, status = status.HTTP_404_NOT_FOUND)
    except ObjectDoesNotExist:
        return Response({"error" : "Meeting code n'existe pas"}, status = status.HTTP_404_NOT_FOUND)


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
            return Response({"error" : "Meeting n'existe pas"}, status = status.HTTP_404_NOT_FOUND)
        
        # We verify if he is participant of the meeting
        try:
            participant = Participant.objects.get(userid = pkUser)

            # Create Commentmeeting data model and store it
            serializer = CommentmeetingSerializer(data = request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({"success" : "Comment ajouté"}, status = status.HTTP_200_OK)
            else:
                return Response({"error" : "Format de données invalide"}, status = status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({"error" : "Participant n'existe pas"}, status = status.HTTP_404_NOT_FOUND)
    except ObjectDoesNotExist:
        return Response({"error" : "Meeting code n'existe pas"}, status = status.HTTP_404_NOT_FOUND)



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
        return Response({"error" : "Comments n'existe pas pour cette réunion"}, status = status.HTTP_404_NOT_FOUND)



# Launch a Whiteboard  -----------------
@swagger_auto_schema(method='post', request_body=WhiteboardSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def LaunchWhiteboard(request):
    # Create whiteboard data model and store it
    serializer = WhiteboardSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

        return Response({"success" : "Tableau de note démarré"}, status = status.HTTP_200_OK)
    else:
        return Response({"error" : "Format de données invalide"}, status = status.HTTP_400_BAD_REQUEST)




# Add comment of whiteboard -------------
@swagger_auto_schema(method='put', request_body=CommentwhiteboardSerializer)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def AddCommentWhiteboard(request, whiteName):
    # Check if whiteName is valid
    try:
        # We get whiteName of current whiteboard 
        whiteboard = Whiteboard.objects.get(whitename = whiteName)

        # We cast field whiteboardid with current whiteboard id
        request.data['whiteboardid'] = whiteboard.id

        # Create Commentwhiteboard data model and store it
        serializer = CommentwhiteboardSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"success" : "Comment ajouté"}, status = status.HTTP_200_OK)
        else:
            return Response({"error" : "Format de données invalide"}, status = status.HTTP_400_BAD_REQUEST)
    except ObjectDoesNotExist:
        return Response({"error" : "Whiteboard code n'existe pas"}, status = status.HTTP_404_NOT_FOUND)




# Display Comment of Whiteboard  -----------------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ViewCommentWhiteboard(request, whiteName):
    # Check if whiteboard is valid
    try:
        whiteboard = Whiteboard.objects.get(whitename = whiteName)

        # Get all comments of whiteboard
        commentwhiteboard = Commentwhiteboard.objects.all().filter(whiteboardid = whiteboard.id)

        # We convert data in valid format
        serialization = CommentwhiteboardSerializer(commentwhiteboard, many = True)

        return Response({"response" : serialization.data}, status = status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({"error" : "Comments n'existe pas pour ce tableau de note"}, status = status.HTTP_404_NOT_FOUND)


# Define socket view

