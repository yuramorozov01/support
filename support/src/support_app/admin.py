from django.contrib import admin
from django.contrib.auth.models import Permission

from django.contrib.auth.models import Permission

# def add_group_permissions():
#     # Support group
#     group, created = Group.objects.get_or_create(name='support_user') 
#     if created:
#         can_view_all_tickets = Permission.objects.get(codename='can_view_all_tickets')
#         group.permissions.add(can_view_all_tickets)

#         can_change_status = Permission.objects.get(codename='can_change_status')
#         group.permissions.add(can_change_status)

#         can_message_in_different_tickets = Permission.objects.get(codename='can_message_in_different_tickets')
#         group.permissions.add(can_message_in_different_tickets)

#         logger.info('Support group has been created successfully!')
