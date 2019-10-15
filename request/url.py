from django.urls import path, include
from uber.views import UberView
from cabify.views import CabifyView
from request.views import RequestView
from metro.views import MetroView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('test', RequestView)
router.register('uber-service', UberView)
router.register('cabify-services', CabifyView)
router.register('metro-services', MetroView)

urlpatterns = [
    path('', include(router.urls))

]