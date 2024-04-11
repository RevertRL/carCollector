from django.shortcuts import render

# Create your views here.
cars = [
    {'make': 'Dodge', 'model': 'Charger', 'year': '1969', 'description': 'General Lee', 'image_url': 'https://i.imgur.com/yCL886w.jpeg'},
    {'make': 'Plymouth', 'model': 'Road Runner', 'year': '1968', 'description': 'Best Road Runner year by popular opinion', 'image_url': 'https://i.imgur.com/ApoNP3q.jpeg'},
    {'make': 'Plymouth', 'model': 'Superbird', 'year': '1970', 'description': 'Richard Pettys 1970 NASCAR car', 'image_url':'https://i.imgur.com/J0rTd5z.jpg'},
]


def home(request):
  return render(request, 'home.html')

def about_view(request):
    return render(request, 'about.html')

def cars_index(request):
    return render(request, 'cars/index.html', {
    'cars': cars
})