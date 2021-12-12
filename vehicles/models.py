from django.db import models

from drivers.models import Driver


class Vehicle(models.Model):
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    plate_number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return self.model
