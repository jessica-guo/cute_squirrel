from django.shortcuts import render
from sightings.models import squirrel

def all_map(request):
    # A view that shows a map that displays the location of the squirrel sightings
    squirrels = squirrel.objects.all()
    context = {
        'squirrels':squirrels,
    }
    return render(request, 'map/map.html', context)
