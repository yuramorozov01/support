from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    '''Ticket message model
    Ticket message can be left in a ticket
    Message can be replied only by a ticket author or a support.
    First message in ticket doesn't have a parent message.
    '''

    ticket = models.ForeignKey(
        'ticket_app.Ticket', 
        verbose_name='Ticket', 
        on_delete=models.CASCADE, 
        related_name='messages'
    )
    text = models.TextField('Message', max_length=8192)
    created_at = models.DateTimeField('Message time', auto_now_add=True)
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE, related_name='messages')
    parent = models.ForeignKey(
        'self', 
        verbose_name='parent', 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='children'
    )

    def __str__(self):
        return '{}: {}'.format(self.author, self.text)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
        permissions = [
            ('can_message_in_different_tickets', 'Can send message in different tickets')
        ]
