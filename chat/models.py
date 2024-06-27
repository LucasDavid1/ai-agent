from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    instrument = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.instrument})"


class Band(models.Model):
    name = models.CharField(max_length=100)
    formation_year = models.IntegerField()
    genre = models.CharField(max_length=50)
    members = models.ManyToManyField(Artist, related_name='bands')

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    genre = models.CharField(max_length=50)
    band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name='albums')

    def __str__(self):
        return f"{self.title} by {self.band.name}"
