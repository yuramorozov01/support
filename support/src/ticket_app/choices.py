from django.db import models


class StatusChoices(models.IntegerChoices):
    OPEN = 0, _('Open')
    CLOSED = 1, _('Closed')
    FREEZED = 2, _('Freezed')

    __empty__ = _('(Open)')
