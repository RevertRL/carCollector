from django.db import models
from django.urls import reverse
# Create your models here.


CARSHOWS = (
    ('Chi' , 'Chicago Auto Show'),
    ('NAi', 'North American International Auto Show'),
    ('SFi', 'SanFrancisco International Auto Show'),
    ('NYi', 'New York International Auto Show'),
    ('GNR', 'Grand National Roadster Show')
)



class Car( models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    description = models.TextField(max_length=200)
    image_url = models.CharField(max_length=100, default='https://i.imgur.com/A2EDuDT.png')
    
    
    def __str__(self):
        return f'{self.description} ({self.id})'
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={'car_id': self.id})
    
class Carshow(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=30)
    carshow = models.CharField(
        max_length=30, 
            choices=CARSHOWS,
            default=CARSHOWS[0][0]
        )
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_carshow_display()} on {self.date}"