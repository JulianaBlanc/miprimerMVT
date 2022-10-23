from unittest.util import _MAX_LENGTH
from django.db import models
# Create your models here.

class Familiares (models.Model):
    parentesco = models.CharField (max_length=30,null=True)
    nombre = models.CharField (max_length=30)
    edad = models.IntegerField()
