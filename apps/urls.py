from django.urls import path, include

urlpatterns = [
    path(
        'item/',
        include('apps.item.api.urls'),
    ),
]
