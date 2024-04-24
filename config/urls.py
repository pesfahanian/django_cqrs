from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from rest_framework import permissions

if settings.DEBUG:
    from drf_yasg import openapi
    from drf_yasg.views import get_schema_view

urlpatterns = [
    path(
        'admin/',
        admin.site.urls,
    ),
    path(
        'healthcheck/',
        include('health_check.urls'),
    ),
    path(
        'api/v1/',
        include('apps.urls'),
    ),
]

if settings.DEBUG:
    schema_view = get_schema_view(
        openapi.Info(
            title='Django-CQRS',
            default_version='0.1.0',
            description=
            'Swagger UI for `Django-CQRS` backend service API Schema.',
        ),
        permission_classes=[
            permissions.AllowAny,
        ],
        public=True,
    )
    urlpatterns += [
        path(
            'swagger/',
            schema_view.with_ui('swagger'),
            name='api-schema-swagger-ui',
        ),
    ]

admin.site.site_header = 'Django-CQRS Administration Panel'
admin.site.index_title = 'Django-CQRS'
admin.site.site_title = 'Django-CQRS Admin'
