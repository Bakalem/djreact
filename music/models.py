from django.db import models

# Create your models here.

class Music(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

def __str__(self):
    return self.titre