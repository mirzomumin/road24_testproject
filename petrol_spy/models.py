from django.db import models
from django.contrib.auth.models import User


class Station(models.Model):
    name = models.CharField(max_length=32)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    is_open = models.BooleanField()
    is_available = models.BooleanField()


class Fuel(models.Model):
    class Types(models.TextChoices):
        BENZIN_80 = 'BENZIN_80', 'Benzin 80'
        BENZIN_91 = 'BENZIN_91', 'Benzin 91'
        BENZIN_92 = 'BENZIN_92', 'Benzin 92'
        BENZIN_95 = 'BENZIN_95', 'Benzin 95'
        BENZIN_98 = 'BENZIN_98', 'Benzin 98'
        BENZIN_100 = 'BENZIN_100', 'Benzin 100'
        METAN = 'METAN', 'Metan'
        PROPAN = 'PROPAN', 'Propan'

    type = models.CharField(choices=Types.choices, max_length=32)
    station = models.ForeignKey(Station, related_name="fuels", on_delete=models.CASCADE)
    is_available = models.BooleanField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reports")
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE)
    is_available = models.BooleanField()
    price = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['created_at', 'user']),
        ]