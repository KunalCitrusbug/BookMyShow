from django.db import models
from multiselectfield import MultiSelectField


# Create your models here.

class Language(models.Model):
    language = models.CharField(max_length=150)

    def __str__(self):
        return self.language


class Movie(models.Model):
    TAG = (
        ("Drama", "Drama"),
        ("Comedy", "Comedy"),
        ("Action", "Action"),
        ("Animations", "Animations"),

    )
    TYPE = (
        ("2D", "2D"),
        ("3D", "3D")
    )
    name = models.CharField(max_length=150)
    image = models.ImageField(null=True, blank=True)
    banner = models.ImageField(null=True, blank=True)
    tags = MultiSelectField(
        choices=TAG, max_length=100, null=True, blank=True
    )
    release_date = models.DateField()
    type = MultiSelectField(
        choices=TYPE, max_length=100, null=True, blank=True
    )
    language = models.ManyToManyField(Language)
    recommended = models.BooleanField(default=False)
    duration = models.CharField(blank=True,null=True,max_length=100)
    movie_description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name
