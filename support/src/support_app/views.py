from rest_framework import permissions, viewsets

from .models import Message, Ticket
from .serializers import (MessageCreateSerializer, MessageDetailsSerializer,
                          MessageShortDetailsSerializer,
                          TicketCreateSerializer, TicketDetailsSerializer,
                          TicketShortDetailsSerializer, TicketUpdateSerializer)


class TicketViewSet(viewsets.ModelViewSet):
    '''
    create:
        Create a new ticket.

    retrieve:
        Return the specified ticket.

    list:
        Return a list of all user's tickets.

    destroy:
        Delete a ticket.
        Only author can delete this ticket.

    update:
        Update a ticket.
        Author can change all exclude status.

    partial_update:
        Update a ticket.
        Author can change all exclude status.
    '''

    queryset = Ticket.objects.all().filter(author=self.request.user)
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return TicketCreateSerializer
        elif self.action == 'retrieve':
            return TicketDetailsSerializer
        elif self.action == 'list':
            return TicketShortDetailsSerializer
        elif self.action == 'update':
            return TicketUpdateSerializer
        elif self.action == 'partial_update':
            return TicketUpdateSerializer


class MessageViewSet(viewsets.ModelViewSet):
    '''
    create:
        Create a new message.

    retrieve:
        Return the specified message.

    list:
        Return a list of all user's message.

    destroy:
        Delete a message.
        Only author can delete his message.

    update:
        Update a message.

    partial_update:
        Update a message.

    '''

    queryset = Message.objects.all().filter(author=self.request.user)
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return MessageCreateSerializer
        elif self.action == 'retrieve':
            return MessageDetailsSerializer
        elif self.action == 'list':
            return MessageShortDetailsSerializer
        elif self.action == 'update':
            return MessageCreateSerializer
        elif self.action == 'partial_update':
            return MessageCreateSerializer
