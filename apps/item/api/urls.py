from django.urls import path

from apps.item.api import views

urlpatterns = [
    path(
        route='',
        view=views.ItemListAPIView.as_view(),
        name='item-list',
    ),
]
