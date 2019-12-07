from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import squirrel
from .forms import SqForm
import pandas as pd

def stats(request):
    squirrels = squirrel.objects.all()
    columns = [field.name for field in squirrel._meta.fields]
    AM=pd.DataFrame(list(squirrels.values())).groupby('Shift').count()['Unique_Squirrel_ID'][0]
    PM=pd.DataFrame(list(squirrels.values())).groupby('Shift').count()['Unique_Squirrel_ID'][1]
    Adult=pd.DataFrame(list(squirrels.values())).groupby('Age').count()['Unique_Squirrel_ID'][0]
    Juvenile=pd.DataFrame(list(squirrels.values())).groupby('Age').count()['Unique_Squirrel_ID'][1]
    Grey=pd.DataFrame(list(squirrels.values())).groupby('Primary_Fur_Color').count()['Unique_Squirrel_ID'][0]
    Cinnamon=pd.DataFrame(list(squirrels.values())).groupby('Primary_Fur_Color').count()['Unique_Squirrel_ID'][1]
    Black=pd.DataFrame(list(squirrels.values())).groupby('Primary_Fur_Color').count()['Unique_Squirrel_ID'][2]
    Ground_Plane=pd.DataFrame(list(squirrels.values())).groupby('Location').count()['Unique_Squirrel_ID'][0]
    Above_Ground=pd.DataFrame(list(squirrels.values())).groupby('Location').count()['Unique_Squirrel_ID'][1]

    context = {
            'AM':AM,
            'PM':PM,
            'Adult':Adult,
            'Juvenile':Juvenile,
            'Grey':Grey,
            'Cinnamon':Cinnamon,
            'Black':Black,
            'Ground_Plane':Ground_Plane,
            'Above_Ground':Above_Ground,
            }
    return render(request, 'sightings/stats.html',context)


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
