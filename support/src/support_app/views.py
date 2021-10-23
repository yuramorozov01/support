from rest_framework import permissions, viewsets
from .models import Message, Ticket
from .serializers import TicketCreateSerializer


class TicketViewSet(viewsets.ModelViewSet):
    '''
    create:
        Create a new ticket.
    '''

    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return TicketCreateSerializer
