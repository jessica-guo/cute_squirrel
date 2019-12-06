from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import squirrel
from .forms import SqForm

def all_squirrel(request):
    # A view to list all squirrels' unique id 
    squirrels = squirrel.objects.all()
    context = {
        'squirrels':squirrels,
    }
    return render(request, 'sightings/all.html', context)

def update_sightings(request,Unique_Squirrel_ID):
    # A view to update a particular sighting
    sighting = squirrel.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method == 'POST':
        form = SqForm(request.POST, instance=sighting)
        # check data is valid to post
        if form.is_valid():
            form.save()
            return redirect('/sightings')
    else:
        form = SqForm(instance=sighting)

    context = {
        'form': form,
    }

    return render(request, 'sightings/update.html', context)

def add_sightings(request):
    # A view to create a new sighting
    if request.method == 'POST':
        form = SqForm(request.POST)
        # check data is calid to add
        if form.is_valid():
            form.save()
            return redirect('/sightings')
    else:
         form = SqForm()

    context = {
        'form': form,
    }

    return render(request, 'sightings/update.html', context)

# Create your views here.
