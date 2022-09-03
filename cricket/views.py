from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from cricket.models import Cricket, Terrarium
from cricket.serializers import (
    CricketSerializer,
    TerrariumDetailSerializer,
    TerrariumSerializer,
)
from utils.viewset_mixins import DualViewSetMixin


class CricketViewSet(ModelViewSet):
    queryset = Cricket.objects.select_related('location')
    serializer_class = CricketSerializer
    # permission_classes = [permissions.IsAuthenticated]


class TerrariumViewset(ModelViewSet, DualViewSetMixin):
    queryset = Terrarium.objects.all()
    detail_queryset = Terrarium.objects.prefetch_related('accesory')
    serializer_class = TerrariumSerializer
    detail_serializer_class = TerrariumDetailSerializer
    # permission_classes = [permissions.IsAuthenticated]
