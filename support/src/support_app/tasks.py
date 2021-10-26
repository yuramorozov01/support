from celery import shared_task
from django.core.mail import send_mail
from decouple import config


@shared_task
def send_new_message_email(email, ticket_title, message_text):
    send_mail(
        'Ticket "{}"'.format(ticket_title),
        'You have been received new message in your ticket:\n{}'.format(message_text),
        config('EMAIL_HOST_USER'),
        [email],
        fail_silently=False,
    )
    return True