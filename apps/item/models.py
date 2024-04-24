from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models import BaseModel, TemporalModel


class Item(BaseModel, TemporalModel):

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    name = models.CharField(
        verbose_name=_('Name'),
        max_length=256,
    )

    price = models.PositiveBigIntegerField(verbose_name=_('Price'))

    def __str__(self) -> str:
        return self.name
