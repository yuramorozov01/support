from message_app.serializers import MessageDetailsSerializer
from rest_framework import serializers
from support_app.serializers import CustomUserSerializer
from ticket_app.models import Ticket


class TicketCreateSerializer(serializers.ModelSerializer):
    '''Serializer for creating ticket'''

    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'
        read_only_fields = ['status', 'created_at']


class TicketUpdateSerializer(serializers.ModelSerializer):
    '''Serializer for updating ticket'''

    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'
        read_only_fields = ['author', 'created_at']

    def validate_status(self, value):
        if self.instance and value != self.instance.status:
            raise serializers.ValidationError('Status can be changed only by a support')
        return value


class TicketShortDetailsSerializer(serializers.ModelSerializer):
    '''Serializer for a ticket
    This serializer provides short necessary information about ticket.
    '''

    status = serializers.CharField(source='get_status_display')
    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'


class TicketDetailsSerializer(serializers.ModelSerializer):
    '''Serializer for a specified ticket
    This serializer provides detailed information about ticket.
    '''

    status = serializers.CharField(source='get_status_display')
    author = CustomUserSerializer(read_only=True)
    messages = MessageDetailsSerializer(read_only=True, many=True)

    class Meta:
        model = Ticket
        fields = '__all__'
