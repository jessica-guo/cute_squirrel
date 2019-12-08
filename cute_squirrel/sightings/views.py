from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import squirrel
from .forms import SqForm

# the package used for visualization
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
from matplotlib import pyplot as plt
import io
import matplotlib.pyplot as plt; plt.rcdefaults()

def stats(request):
    # A view to count the number of each feature
    AM=squirrel.objects.filter(Shift='AM').count()
    PM=squirrel.objects.filter(Shift='PM').count()
    Adult=squirrel.objects.filter(Age='Adult').count()
    Juvenile=squirrel.objects.filter(Age='Juvenile').count()
    Gray=squirrel.objects.filter(Primary_Fur_Color='Gray').count()
    Cinnamon=squirrel.objects.filter(Primary_Fur_Color='Cinnamon').count()
    Black=squirrel.objects.filter(Primary_Fur_Color='Black').count()
    Ground_Plane=squirrel.objects.filter(Location='Ground Plane').count()
    Above_Ground=squirrel.objects.filter(Location='Above Ground').count()

    context = {
            'AM':AM,
            'PM':PM,
            'Adult':Adult,
            'Juvenile':Juvenile,
            'Gray':Gray,
            'Cinnamon':Cinnamon,
            'Black':Black,
            'Ground_Plane':Ground_Plane,
            'Above_Ground':Above_Ground,
            }
    return render(request, 'sightings/stats.html',context)

def pie_graph(request):
    # A view to show four pie graoh in one page
    fig = Figure()
    canvas = FigureCanvas(fig)
    squirrels = squirrel.objects.all()
    columns = [field.name for field in squirrel._meta.fields]
    df = pd.DataFrame(list(squirrels.values()),columns=columns)
    colors = ['Pink','Salmon', 'Tomato']
    # obtain data used for pie graph
    plt_data_1 = df.groupby('Shift').count()['Unique_Squirrel_ID']
    plt_data_2 = df.groupby('Age').count()['Unique_Squirrel_ID'][1:]
    plt_data_3 = df.groupby('Primary_Fur_Color').count()['Unique_Squirrel_ID']
    plt_data_4 = df.groupby('Location').count()['Unique_Squirrel_ID']
    # draw pie graoh
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


def bar_graph(request):
    # A view to show stack bar graph about all boolean fields
    fig = Figure()
    canvas = FigureCanvas(fig)
    squirrels = squirrel.objects.all()
    columns = [field.name for field in squirrel._meta.fields]
    df = pd.DataFrame(list(squirrels.values()),columns=columns)
    # obtain data used for bar graph
    plt_data_running = df.groupby('Running').count()['Unique_Squirrel_ID']
    plt_data_chasing = df.groupby('Chasing').count()['Unique_Squirrel_ID']
    plt_data_eating = df.groupby('Eating').count()['Unique_Squirrel_ID']
    plt_data_foraging = df.groupby('Foraging').count()['Unique_Squirrel_ID']
    plt_data_kuks = df.groupby('Kuks').count()['Unique_Squirrel_ID']
    plt_data_quaas = df.groupby('Quaas').count()['Unique_Squirrel_ID']
    plt_data_moans = df.groupby('Moans').count()['Unique_Squirrel_ID']
    plt_data_tail_flags = df.groupby('Tail_flags').count()['Unique_Squirrel_ID']
    plt_data_tail_twitches = df.groupby('Tail_twitches').count()['Unique_Squirrel_ID']
    plt_data_approaches = df.groupby('Approaches').count()['Unique_Squirrel_ID']
    plt_data_indifferent = df.groupby('Indifferent').count()['Unique_Squirrel_ID']
    plt_data_runs_from = df.groupby('Runs_from').count()['Unique_Squirrel_ID']
    # concat all series into a dataframe
    plt_data_5 = pd.concat([plt_data_running,plt_data_chasing,plt_data_eating,plt_data_foraging,
                            plt_data_kuks,plt_data_quaas,plt_data_moans,plt_data_tail_flags,
                            plt_data_tail_twitches,plt_data_approaches,plt_data_indifferent,plt_data_runs_from],
                            axis=1)
    fig,ax=plt.subplots(figsize=(12,8))
    # x-label for stacj bar graph
    x=['Running','Chasing','Eating','Foraging','Kuks','Quaas','Moans','Tail flags','Tail twitches','Approaches','Indifferent','Runs from']
    # value used to draw stack bar graph
    value = plt_data_5.values.T
    v1 = [i[0]+i[1] for i in value] # the top part of the stack bar graph
    v2 = [i[1] for i in value] # the bottom part of the stack bar graph
    ax.bar(x,v1,color='Pink')
    ax.bar(x,v2,color='Salmon')
    ax.set(xlabel='Activities',title='Squirrels Activities')
    plt.xticks(rotation=30)
    # add tags at the top of every bar
    for a,b in zip(x,v1):
        plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=10)
    for a,b in zip(x,v2):
        plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=10)
    # set legend
    ax.legend(['False','True'],loc='lower right',fontsize=15)

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
        form = SqForm(request.POST or None, instance=sighting)
        # check data is valid to post
        if form.is_valid():
            form.save()
            return redirect('/sightings/')
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
            return redirect('/sightings/')
    else:
         form = SqForm()

    context = {
        'form': form,
    }

    return render(request, 'sightings/update.html', context)

def homepage(request):
    return render(request, 'sightings/homepage.html')
# Create your views here.
