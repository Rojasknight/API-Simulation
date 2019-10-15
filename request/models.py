from django.db import models


class Request(models.Model):
    #name = models.CharField(max_length=1000)
    #payload = models.CharField(max_length=1000)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name