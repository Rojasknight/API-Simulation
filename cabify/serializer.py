from rest_framework import serializers
from .models import Cabify


class CabifySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cabify
        fields = ('url', 'car_model','start_city', 'latitude', 'longitude','currency_code', 'rate')