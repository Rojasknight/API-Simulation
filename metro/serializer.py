from rest_framework import serializers
from .models import Metro


class MetroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Metro
        fields = ('url', 'name_station','start_city', 'latitude', 'longitude','currency_code', 'rate')