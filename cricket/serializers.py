from rest_framework import serializers
from cricket.models import Cricket


class CricketSerializer(serializers.ModelSerializer):
    location_name = serializers.CharField(source='location.name', read_only=True)

    class Meta:
        model = Cricket
        fields = '__all__'
