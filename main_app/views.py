from django.shortcuts import render

# Create your views here.
cars = [
    {'make': 'Dodge', 'model': 'Charger', 'year': '1969', 'description': 'General Lee'},
    {'make': 'Plymouth', 'model': 'Road Runner', 'year': '1968', 'description': 'Best Road Runner year'},
    {'make': 'Dodge', 'model': 'Charger Daytona', 'year': '1973', 'description': 'Richard Pettys'},
]


def home(request):
  return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def cars_index(request):
    return render(request, 'cars/index.html', {
    'cars': cars
})