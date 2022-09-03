from rest_framework import serializers
from cricket.models import Accessory, Cricket, Terrarium


class CricketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cricket
        fields = '__all__'

    location_name = serializers.CharField(source='location.name', read_only=True)


class AccessorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessory
        fields = '__all__'


class TerrariumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terrarium
        fields = '__all__'


class TerrariumDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terrarium
        fields = '__all__'

    accessories = AccessorySerializer(read_only=True)
