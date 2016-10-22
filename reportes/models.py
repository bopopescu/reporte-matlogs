from django.db import models

# Create your models here.
class AGAFF(models.Model):
    log = models.CharField(max_length=80)
    ambiente = models.CharField(max_length=20)
    error = models.CharField(max_length=200)
    fecha = models.DateTimeField('fecha error')
    detalle = models.CharField(max_length=10000)


class COB(models.Model):
    log = models.CharField(max_length=70)
    ambiente = models.CharField(max_length=20)
    error = models.CharField(max_length=200)
    fecha = models.DateTimeField('fecha error')
    detalle = models.CharField(max_length=10000)