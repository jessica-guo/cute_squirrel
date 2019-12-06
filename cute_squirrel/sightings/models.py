from django.db import models
from django.db import models
from django.utils.translation import gettext as _

class squirrel(models.Model):
    GROUND_PLANE = 'ground plane'
    ABOVE_GROUND = 'above ground'
    OTHERS = ''

    LOCATION_CHOICES = (
        (GROUND_PLANE, 'ground plane'),
        (ABOVE_GROUND, 'above ground'),
        (OTHERS, ''),
    )

    Location = models.CharField(
        help_text=_('squirrel location'),
        max_length=50,
        choices=LOCATION_CHOICES,
        default=OTHERS,
    )

    Specific_Location = models.CharField(
        help_text=_('Specific Location of squirrels'),
        max_length=100,
    )

    Running = models.BooleanField(
        default=False,
    )

    Chasing = models.BooleanField(
        default=False,
    )

    Climbing = models.BooleanField(
        default=False,
    )

    Eating = models.BooleanField(
        default=False,
    )

    Foraging = models.BooleanField(
        default=False,
    )

    Other_Activities = models.CharField(
        help_text=_('Other activities squirrels are doing'),
        max_length=100,
    )

    Kuks = models.BooleanField(
        default=False,
    )

    Quaas = models.BooleanField(
        default=False,
    )
    
    Moans = models.BooleanField(
        default=False,
    )
   
    Tail_flags = models.BooleanField(
        default=False,
    )

    Tail_twitches = models.BooleanField(
        default=False,
    )

    Approaches = models.BooleanField(
        default=False,
    )
    
    Indifferent = models.BooleanField(
        default=False,
    )

    Runs_from = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.Unique_Squirrel_ID
# Create your models here.
