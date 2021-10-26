from django.contrib import admin
from django.contrib.auth.models import Group, Permission

# Register your models here.

def add_group_permissions():
    # Support group
    group, created = Group.objects.get_or_create(name='support_user') 
    if created:
        can_view_all_tickets = Permission.objects.get(codename='can_view_all_tickets')
        group.permissions.add(can_view_all_tickets)

        can_change_status = Permission.objects.get(codename='can_change_status')
        group.permissions.add(can_change_status)

        can_message_in_different_tickets = Permission.objects.get(codename='can_message_in_different_tickets')
        group.permissions.add(can_message_in_different_tickets)

add_group_permissions()
