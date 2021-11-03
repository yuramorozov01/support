from django.contrib.auth import get_user_model
from message_app.models import Message
from rest_framework import serializers
from support_app.tasks import send_new_message_email
from ticket_app.models import Ticket


class CustomUserSerializer(serializers.ModelSerializer):
    '''Serializer for an user'''

    class Meta:
        model = get_user_model()
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

    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ['created_at']

    def validate(self, data):
        # Check that child is in the same ticket as parent
        if data.get('parent'):
            if data.get('parent').ticket != data.get('ticket'):
                raise serializers.ValidationError('Child message must be in the same ticket as parent message!')
        return data

    def create(self, validated_data):
        ticket = Ticket.objects.get(pk=validated_data.get('ticket').id)
        if ticket.author.email:
            send_new_message_email.delay(ticket.author.email, ticket.title, validated_data.get('text'))
        return super(SupportMessageCreateSerializer, self).create(validated_data)
