from django.contrib.auth.models import User
from .models import Message, Ticket
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
    '''Serializer for an user'''

    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class TicketCreateSerializer(serializers.ModelSerializer):
    '''Serializer for creating ticket'''

    class Meta:
        model = Ticket
        fields = '__all__'
        extra_kwargs = {'author': {'default': serializers.CurrentUserDefault()}}


class TicketUpdateSerializer(serializers.ModelSerializer):
    '''Serializer for updating ticket'''

    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'
        extra_kwargs = {'author': {'default': serializers.CurrentUserDefault()}}

    def validate_status(self, value):
        if self.instance and value != self.instance.status:
            raise serializers.ValidationError('Status can be changed only by a support')
        return value


class TicketDetailsSerializer(serializers.ModelSerializer):
    '''Serializer for a specified ticket
    This serializer provides detailed information about ticket.
    '''

    status = serializers.CharField(source='get_status_display')
    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'


class TicketShortDetailsSerializer(serializers.ModelSerializer):
    '''Serializer for a ticket
    This serializer provides short necessary information about ticket.
    '''

    status = serializers.CharField(source='get_status_display')
    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'


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
