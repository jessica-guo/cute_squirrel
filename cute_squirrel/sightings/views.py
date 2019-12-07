from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import squirrel
from .forms import SqForm

# the package used for stat
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
from matplotlib import pyplot as plt
import io
import matplotlib.pyplot as plt; plt.rcdefaults()

def graphs(request):
    fig = Figure()
    canvas = FigureCanvas(fig)
    squirrels = squirrel.objects.all()
    columns = [field.name for field in squirrel._meta.fields]
    df = pd.DataFrame(list(squirrels.values()),columns=columns)
    colors = ['Pink','Salmon', 'Tomato']

    plt_data_1 = df.groupby('Shift').count()['Unique_Squirrel_ID']
    plt_data_2 = df.groupby('Age').count()['Unique_Squirrel_ID'][1:]
    plt_data_3 = df.groupby('Primary_Fur_Color').count()['Unique_Squirrel_ID']
    plt_data_4 = df.groupby('Location').count()['Unique_Squirrel_ID']
    plt.figure(figsize=(12,12))
    plt.subplot(2,2,1)
    plt.pie(plt_data_1, labels=plt_data_1.index, labeldistance=1.1, shadow=False, startangle=None, pctdistance=0.6, autopct='%0.01f%%', colors=colors)
    plt.title('When the sightings happen')
    plt.subplot(2,2,2)
    plt.pie(plt_data_2, labels=plt_data_2.index, labeldistance=1.1, shadow=False, startangle=None, pctdistance=0.6, autopct='%0.01f%%', colors=colors)
    plt.title('The age of squirrels')
    plt.subplot(2,2,3)
    plt.pie(plt_data_3, labels=plt_data_3.index, labeldistance=1.1, shadow=False, startangle=None, pctdistance=0.6, autopct='%0.01f%%',colors=colors)
    plt.title('Primary Fur color of squirrels')
    plt.subplot(2,2,4)
    plt.pie(plt_data_4, labels=plt_data_4.index, labeldistance=1.1, shadow=False, startangle=None, pctdistance=0.6, autopct='%0.01f%%',colors=colors)
    plt.title('The location of squirrels')
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(fig)
    response = HttpResponse(buf.getvalue(),content_type='image/png')
    return response

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
