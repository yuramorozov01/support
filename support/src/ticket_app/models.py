from django.contrib.auth.models import get_user_model
from django.db import models
from ticket_app.choices import StatusChoices


class Ticket(models.Model):
    '''Ticket Model
    User can send a ticket with question to a support user.
    Ticket status can be changed only by a support user.
    '''

    title = models.CharField('Title', max_length=128)
    status = models.IntegerField(choices=StatusChoices.choices, default=StatusChoices.OPEN)
    text = models.TextField('Question', max_length=8192)
    author = models.ForeignKey(
        get_user_model(), 
        verbose_name='Author', 
        on_delete=models.CASCADE, 
        related_name='tickets'
    )
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
