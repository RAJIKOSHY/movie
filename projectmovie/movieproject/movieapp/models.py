from django.db import models

# Create your models here.
class movie(models.Model):
    name = models.CharField(max_length=250)
    details = models.TextField()
    year = models.IntegerField()
    pic = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name