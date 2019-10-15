from django.http import HttpRequest
from django.shortcuts import render
from rest_framework import viewsets


from uber.serializers import UberSerializer
from .models import Uber


class UberView(viewsets.ModelViewSet):
    queryset = Uber.objects.all()
    serializer_class = UberSerializer

