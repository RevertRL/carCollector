from django.shortcuts import render, redirect
from .models import Car, Carshow, CARSHOWS
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse



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
    all_cars = Car.objects.all()
    carshows_not_attending_dict = {}
    
    for each_car in all_cars:
        if each_car.id != car.id: 
            carshows_not_attending = Carshow.objects.filter(car=each_car)
            carshows_not_attending_dict[each_car.id] = carshows_not_attending
    
    return render(request, 'cars/detail.html', {
        'car': car,
        'carshows_not_attending_dict': carshows_not_attending_dict
    })
    
def car_attend(request, car_id, carshow_id):
    if request.method == 'POST':
        car = Car.objects.get(id=car_id)
        carshow = Carshow.objects.get(id=carshow_id)
        carshow.car = car
        carshow.save()
        return redirect('detail', car_id=car_id)
    else:
        return redirect('home')

class CarCreate(CreateView):
    model = Car
    fields = '__all__'
    
class CarUpdate(UpdateView):
  model = Car
  fields = ['model', 'make', 'year', 'description']

class CarDelete(DeleteView):
  model = Car
  success_url = '/cars'
