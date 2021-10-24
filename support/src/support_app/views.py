from rest_framework import permissions, viewsets
from .models import Message, Ticket
from .serializers import MessageCreateSerializer, TicketCreateSerializer, TicketDetailsSerializer, TicketListSerializer, TicketUpdateSerializer


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

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.action == 'retrieve':
            return Ticket.objects.all().filter(author=self.request.user)
        elif self.action == 'list':
            return Ticket.objects.all().filter(author=self.request.user)
        elif self.action == 'destroy':
            return Ticket.objects.all().filter(author=self.request.user)
        elif self.action == 'update':
            return Ticket.objects.all().filter(author=self.request.user)
        elif self.action == 'partial_update':
            return Ticket.objects.all().filter(author=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return TicketCreateSerializer
        elif self.action == 'retrieve':
            return TicketDetailsSerializer
        elif self.action == 'list':
            return TicketListSerializer
        elif self.action == 'update':
            return TicketUpdateSerializer
        elif self.action == 'partial_update':
            return TicketUpdateSerializer


class MessageViewSet(viewsets.ModelViewSet):
    '''
    create:
        Create a new message.

    '''

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        pass

    def get_serializer_class(self):
        if self.action == 'create':
            return MessageCreateSerializer
        