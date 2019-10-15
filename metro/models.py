from django.db import models


class Metro(models.Model):
    name_station = models.CharField(max_length=1000)
    start_city = models.CharField(max_length=1000)
    latitude = models.CharField(max_length=1000)
    longitude = models.CharField(max_length=1000)
    currency_code = models.CharField(max_length=1000)
    rate = models.CharField(max_length=1000)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name