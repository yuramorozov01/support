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
    '''Serializer for a specified ticket'''

    status = serializers.CharField(source='get_status_display')
    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'


class TicketListSerializer(serializers.ModelSerializer):
    '''Serializer for a list of tickets'''

    status = serializers.CharField(source='get_status_display')
    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'
