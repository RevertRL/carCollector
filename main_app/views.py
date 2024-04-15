from django.shortcuts import render
from .models import Car
from django.views.generic.edit import CreateView

# Create your views here.


def home(request):
  return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', 
    {
        'cars': cars
    }
)
    
def cars_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request,'cars/detail.html', { 'car' : car})

class CarCreate(CreateView):
    model = Car
    fields = '__all__'




