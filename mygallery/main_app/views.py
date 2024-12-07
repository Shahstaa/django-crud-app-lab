from django.shortcuts import render
from .models import Sculpture
from django.http import HttpResponse 

def home(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse('<h1>About the Virtual Sculpture Gallery</h1>')

def about(request):
    return render(request, 'about.html')

def sculpture_index(request):
    from .models import Sculpture
    sculptures = Sculpture.objects.all()
    return render(request, 'sculptures/index.html', {'sculptures': sculptures})

def sculpture_detail(request, sculpture_id):
    from .models import Sculpture
    sculpture = Sculpture.objects.get(id=sculpture_id)
    return render(request, 'sculptures/detail.html', {'sculpture': sculpture})


class Sculpture:
    def __init__(self, title, artist, description, year):
        self.title = title
        self.artist = artist
        self.description = description
        self.year = year

sculptures = [
    Sculpture('The Thinker', 'Auguste Rodin', 'A sculpture of a man deep in thought.', 1880),
    Sculpture('Winged Victory of Samothrace', 'Unknown', 'An ancient Greek sculpture of the goddess Nike, symbolizing victory in battle.', -190),
    Sculpture('The Bronze Horseman', 'Etienne Maurice Falconet', 'A statue of Peter the Great on horseback, symbolizing Russian power and victory.', 1782),
    Sculpture('Nefertiti Bust', 'Thutmose', 'A painted limestone bust of Queen Nefertiti, one of the most famous sculptures of ancient Egypt.', -1345)
]
