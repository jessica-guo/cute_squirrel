from django.shortcuts import render
from sightings.models import squirrel

def all_map(request):
    squirrels = squirrel.objects.all()
    context = {
        'squirrels':squirrels,
    }
    return render(request, 'map/map.html', context)
# Create your views here.
