from rest_framework import permissions, viewsets

from support_app.serializers import SupportMessageCreateSerializer

from .models import Message
from .serializers import (MessageCreateSerializer, MessageDetailsSerializer,
                          MessageShortDetailsSerializer)


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

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Message.objects.all().filter(author=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            if self.request.user.has_perm('ticket_app.can_message_in_different_tickets'):
                return SupportMessageCreateSerializer
            return MessageCreateSerializer
        elif self.action == 'retrieve':
            return MessageDetailsSerializer
        elif self.action == 'list':
            return MessageShortDetailsSerializer
        elif self.action == 'update':
            return MessageCreateSerializer
        elif self.action == 'partial_update':
            return MessageCreateSerializer
