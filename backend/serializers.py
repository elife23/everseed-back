from rest_framework import serializers
from .models import *

class CommentmeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentmeeting
        fields  = '__all__'

class CommentwhiteboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentwhiteboard
        fields = '__all__'

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = '__all__'


class MeetingroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meetingroom
        fields = '__all__'

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate_email(self, value):
        norm_email = value.lower()

        if User.objects.filter(email = norm_email).exists():
            raise serializers.ValidationError("Email already exists")
        # Sinon
        return norm_email


class WhiteboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Whiteboard
        fields = '__all__'


"""
Check correct value
def validate(self, data):
    if data['email'] == '':
        raise serializers.ValidationError("Email not good")
        return data
"""