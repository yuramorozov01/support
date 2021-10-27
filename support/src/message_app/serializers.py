from django.contrib.auth.models import User
from rest_framework import serializers
from ticket_app.models import Ticket
from support_app.serializers import CustomUserSerializer

from .models import Message


class MessageCreateSerializer(serializers.ModelSerializer):
    '''Serializer for creating ticket'''

    class Meta:
        model = Message
        fields = '__all__'
        extra_kwargs = {'author': {'default': serializers.CurrentUserDefault()}}

    def validate_ticket(self, value):
        # User can send message only in his own ticket
        # Check that the ticket in which he sends the message belongs to him:
        # Trying to find in his tickets ticket with specified ID (PK - primary key)
        try:
            ticket = Ticket.objects.all().filter(author=self.context['request'].user).get(pk=value.id)
        except Ticket.DoesNotExist:
            raise serializers.ValidationError('Messages in this ticket can be left only by a ticket author!')
        return value

    def validate(self, data):
        # Check that child is in the same ticket as parent
        if data.get('parent'):
            if data.get('parent').ticket != data.get('ticket'):
                raise serializers.ValidationError('Child message must be in the same ticket as parent message!')
        return data


class MessageShortDetailsSerializer(serializers.ModelSerializer):
    '''Serializer for a message
    This serializer uses short information about ticket (uses serializer for short information)
    '''

    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = '__all__'


class RecursiveMessageChildrenSerializer(serializers.Serializer):
    '''Serializer for recursive output children of message model'''

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class FilterMessageListSerrializer(serializers.ListSerializer):
    '''Filter to output only parent messages'''

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class MessageDetailsSerializer(serializers.ModelSerializer):
    '''Serializer for a message
    This serializer provides detailed information about message
    This serializer uses short information about ticket (uses serializer for short information)
    "children" field - related field to parent (get all message where current message is a parent message)
    '''

    author = CustomUserSerializer(read_only=True)
    children = RecursiveMessageChildrenSerializer(read_only=True, many=True)

    class Meta:
        model = Message
        fields = '__all__'

        # Children messages output ...
        # ... with their parent messages at the same nesting level 
        # So to prevent this, we have to filter messages to output ...
        # messages without parent messages - at the zero nesting level have to be ...
        # ... messages without parent messages

        list_serializer_class = FilterMessageListSerrializer
