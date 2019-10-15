from django.http import HttpRequest
from django.shortcuts import render
from rest_framework import viewsets


from cabify.serializer import CabifySerializer
from .models import Cabify


class CabifyView(viewsets.ModelViewSet):
    queryset = Cabify.objects.all()
    serializer_class = CabifySerializer

