from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    IP = models.CharField(max_length=15)
    description = models.CharField(max_length=1000)


    def __str__(self):
        return self.name