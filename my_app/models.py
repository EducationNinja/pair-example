from django.db import models

# Create your models here.

class Thing(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name