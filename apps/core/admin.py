from django.contrib import admin
from django.contrib.auth.models import Group


class TemporalModelAdmin(admin.ModelAdmin):
    readonly_fields = (
        'created_at',
        'updated_at',
    )
    list_display = (
        'created_at',
        'updated_at',
    )
    list_filter = (
        'created_at',
        'updated_at',
    )
    ordering = ('-created_at', )


admin.site.unregister(Group)
