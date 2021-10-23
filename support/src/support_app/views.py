from rest_framework import permissions, viewsets
from .models import Message, Ticket
from .serializers import TicketCreateSerializer, TicketDetailsSerializer


class TicketViewSet(viewsets.ModelViewSet):
    '''
    create:
        Create a new ticket.

    retrieve:
        Return the specified ticket.
    '''

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.action == 'retrieve':
            return Ticket.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return TicketCreateSerializer
        elif self.action == 'retrieve':
            return TicketDetailsSerializer
