from django.urls import path

from . import views

urlpatterns = [
    path('stats/',views.stats),
    path('', views.all_squirrel),
    path('add/', views.add_sightings),
    path('<Unique_Squirrel_ID>/', views.update_sightings),
    path('stats/pie_graph', views.pie_graph),
    path('stats/bar_graph', views.bar_graph),
]
