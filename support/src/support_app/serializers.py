from django.contrib.auth.models import User
from .models import Message, Ticket
from rest_framework import serializers


class TicketCreateSerializer(serializers.ModelSerializer):
    '''Serializer for creating ticket'''

    class Meta:
        model = Ticket
        fields = '__all__'
        extra_kwargs = {'author': {'default': serializers.CurrentUserDefault()}}


class UserSerializer(serializers.ModelSerializer):
    '''Serializer for an user'''

    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class TicketDetailsSerializer(serializers.ModelSerializer):
    '''Serializer for a specified ticket'''

    status = serializers.CharField(source='get_status_display')
    author = UserSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'
