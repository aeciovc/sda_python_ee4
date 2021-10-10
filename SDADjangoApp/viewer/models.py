from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=128)
    is_favorite = models.BooleanField(default=False)


class Movie(models.Model):
    title = models.CharField(max_length=128)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.DO_NOTHING)
    rating = models.IntegerField()
    released = models.DateField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
