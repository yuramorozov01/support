from django.contrib.auth.models import User
from rest_framework import serializers

from ticket_app.models import Ticket
from message_app.models import Message


class CustomUserSerializer(serializers.ModelSerializer):
    '''Serializer for an user'''

    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class AbstractTicketSerializerr(serializers.ModelSerializer):
    
    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = ('__all__')
        read_only_fields = ['title', 'text', 'author', 'created_at']


class SupportTicketUpdateStatusSerializer(AbstractTicketSerializerr):
    '''Serializer to update status of ticket'''
    pass


class SupportMessageCreateSerializer(serializers.ModelSerializer):
    '''Serializer to create messages in diffrenets ticket by a support'''

    class Meta:
        model = Message
        fields = '__all__'
        extra_kwargs = {'author': {'default': serializers.CurrentUserDefault()}}

    def validate(self, data):
        # Check that child is in the same ticket as parent
        if data['parent']:
            if data['parent'].ticket != data['ticket']:
                raise serializers.ValidationError('Child message must be in the same ticket as parent message!')
        return data
