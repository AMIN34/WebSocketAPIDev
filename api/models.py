from django.db import models

# Create your models here.
class SensorData(models.Model):
    voltage = models.CharField(max_length=10)
    current = models.CharField(max_length=10)
    power = models.CharField(max_length=10)
    energy = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return f'SensorData(id={self.id})'