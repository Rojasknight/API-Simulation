from rest_framework import serializers
from .models import Uber


class UberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Uber
        fields = ('url', 'car_model','start_city', 'latitude', 'longitude','currency_code', 'rate')