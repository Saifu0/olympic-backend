from django.db import models


class Event(models.Model):
    is_live = models.BooleanField(default=False)
    date = models.DateField()
    country_a = models.CharField(max_length=100)
    country_b = models.CharField(max_length=100)
    game = models.CharField(max_length=100)

    def __str__(self):
        return self.game + " " + self.country_a + " " + self.country_b


class Country(models.Model):
    name = models.CharField(max_length=100)
    gold = models.IntegerField(default=0)
    silver = models.IntegerField(default=0)
    bronze = models.IntegerField(default=0)
    cheer = models.IntegerField(default=0)

    def __str__(self):
        return self.name
