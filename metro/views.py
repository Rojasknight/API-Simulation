from django.http import HttpRequest
from django.shortcuts import render
from rest_framework import viewsets


from metro.serializer import MetroSerializer
from .models import Metro


class MetroView(viewsets.ModelViewSet):
    queryset = Metro.objects.all()
    serializer_class = MetroSerializer