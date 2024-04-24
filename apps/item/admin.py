from django.contrib import admin

from apps.core.admin import TemporalModelAdmin

from apps.item.models import Item


@admin.register(Item)
class ItemAdmin(TemporalModelAdmin):
    list_display = (
        'name',
        'price',
    ) + TemporalModelAdmin.list_display
    search_fields = ('name', )
