from django.db.models import QuerySet

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.item.api.serializers import ItemSerializer
from apps.item.models import Item


class ItemListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ItemSerializer

    def get_queryset(self) -> QuerySet:
        return Item.objects.using('replica').all().order_by('-created_at')
