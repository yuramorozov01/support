from message_app.models import Message
from message_app.serializers import (MessageCreateSerializer,
                                     MessageDetailsSerializer,
                                     MessageShortDetailsSerializer)
from rest_framework import permissions, viewsets
from support_app.serializers import SupportMessageCreateSerializer


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

    Users with permission 'message_app.can_message_in_different_tickets' can send messages
    in different tickets (user is not an author of ticket)
    '''

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Message.objects.all().filter(author=self.request.user.id)

    def get_serializer_class(self):
        serializers_dict = {
            'create': MessageCreateSerializer,
            'retrieve': MessageDetailsSerializer,
            'list': MessageShortDetailsSerializer,
            'update': MessageCreateSerializer,
            'partial_update': MessageCreateSerializer,
        }
        serializer_class = serializers_dict.get(self.action)
        
        if (self.action == 'create') and self.request.user.has_perm('message_app.can_message_in_different_tickets'):
            serializer_class = SupportMessageCreateSerializer

        return serializer_class
