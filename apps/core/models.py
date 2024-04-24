from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):

    class Meta:
        abstract = True

    id = models.UUIDField(
        verbose_name='ID',
        primary_key=True,
        editable=False,
        default=uuid4,
    )

    def save(self, *args, **kwargs) -> None:
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return str(self.id)


class TemporalModel(models.Model):

    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        verbose_name=_('Created at'),
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        verbose_name=_('Updated at'),
        auto_now=True,
    )
