from django.contrib.auth.models import User
from django.db import models


class Ticket(models.Model):
    '''Ticket Model
    User can send a ticket with question to a support user.
    Ticket status can be changed only by a support user.
    '''

    OPEN_STATUS = 1
    CLOSED_STATUS = 2
    FREEZED_STATUS = 3
    STATUS_CHOICES = (
        (OPEN_STATUS, 'Open'),
        (CLOSED_STATUS, 'Closed'),
        (FREEZED_STATUS, 'Freezed'),
    )

    title = models.CharField('Title', max_length=128)
    status = models.IntegerField(choices=STATUS_CHOICES, default=OPEN_STATUS)
    text = models.TextField('Question', max_length=8192)
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE, related_name='tickets')
    created_at = models.DateTimeField('Creation time', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
        permissions = [
            ('can_view_all_tickets', 'Can view all tickets'),
            ('can_change_status', 'Can change status'),
        ]
