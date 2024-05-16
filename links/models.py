from django.db import models
from django.conf import settings

class Fake(models.Model):
    nombre = models.TextField(blank=True)
    precio = models.TextField(blank=True)
    descripcion = models.TextField(blank=True)
    url = models.URLField()
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)    

class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    link = models.ForeignKey('links.Fake', related_name='votes', on_delete=models.CASCADE)