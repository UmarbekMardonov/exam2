from django.db import models
from django.db.models import Q


class City(models.Model):
    title = models.CharField(max_length=220)

    def __str__(self):
        return self.title


class Street(models.Model):
    title = models.CharField(max_length=220)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Shop(models.Model):
    title = models.CharField(max_length=220)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    home_number = models.CharField(max_length=50)
    open_date = models.TimeField()
    closed_date = models.TimeField()  # timeformat="%H:%M")
    open = models.BooleanField(default=False)

    def __str__(self):
        return self.title
