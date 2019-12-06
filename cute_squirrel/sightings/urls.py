from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_squirrel),
    path('add/', views.add_sightings),
    path('<Unique_Squirrel_ID>/', views.update_sightings),
]
