from django.db import models

# Create your models here.
class Car( models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    description = models.TextField(max_length=200)
    image_url = models.CharField(max_length=100, default='https://i.imgur.com/A2EDuDT.png')
    
    
    def __str__(self):
        return self.description