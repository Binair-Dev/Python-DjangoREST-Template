from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    director = models.ManyToManyField('Director')
    identification_number = models.IntegerField(unique=True)

    def __str__(self):
        return self.title

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"