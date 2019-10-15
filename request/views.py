from django.http import HttpRequest
from django.shortcuts import render
from rest_framework import viewsets


from request.serializers import RequestSerializer
from .models import Request


class RequestView(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

