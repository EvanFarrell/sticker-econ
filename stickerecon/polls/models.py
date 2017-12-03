from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Sticker(models.Model):
    name = models.CharField(max_length=30)
    votes =  models.IntegerField(null=False)
    image = models.FileField()
