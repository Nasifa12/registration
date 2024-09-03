from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_tittle = models.CharField(max_length=250)
    poster = models.ImageField(upload_to="gallery")
    description = models.CharField(max_length=250)
    release_date = models.DateField()
    actors = models.CharField(max_length=250)
    category = models.CharField(max_length=250)

    def ___str___(self):
        return self.name