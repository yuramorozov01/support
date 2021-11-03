from django.db import models
from django.utils.translation import gettext_lazy as _


class StatusChoices(models.IntegerChoices):
    OPEN = 0, _('Open')
    CLOSED = 1, _('Closed')
    FREEZED = 2, _('Freezed')
