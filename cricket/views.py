from rest_framework import viewsets
from rest_framework import permissions

from cricket.models import Cricket
from cricket.serializers import CricketSerializer


class CricketViewSet(viewsets.ModelViewSet):
    queryset = Cricket.objects.select_related('location').all()
    serializer_class = CricketSerializer
    # permission_classes = [permissions.IsAuthenticated]
