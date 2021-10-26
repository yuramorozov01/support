from rest_framework import permissions, viewsets

from support_app.serializers import SupportTicketUpdateStatusSerializer

from .models import Ticket
from .serializers import (TicketCreateSerializer, TicketDetailsSerializer,
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

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.has_perm('ticket_app.can_view_all_tickets'):
            return Ticket.objects.all()

        return Ticket.objects.all().filter(author=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return TicketCreateSerializer
        elif self.action == 'retrieve':
            return TicketDetailsSerializer
        elif self.action == 'list':
            return TicketShortDetailsSerializer
        elif self.action == 'update':
            if self.request.user.has_perm('ticket_app.can_change_status'):
                return SupportTicketUpdateStatusSerializer
            return TicketUpdateSerializer
        elif self.action == 'partial_update':
            if self.request.user.has_perm('ticket_app.can_change_status'):
                return SupportTicketUpdateStatusSerializer
            return TicketUpdateSerializer
