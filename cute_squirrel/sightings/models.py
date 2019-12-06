from django.db import models
from django.utils.translation import gettext as _

class squirrel(models.Model):
    Longitude = models.FloatField(
        help_text=_('Longitude'),
    )

    Latitude = models.FloatField(
        help_text=_('Latitude'),
    )

    Unique_Squirrel_ID = models.CharField(
        help_text=_('Unique Squirrel ID'),
        max_length=100,
    )

    AM = 'AM'
    PM = 'PM'
    OTHERS = ''

    SHIFT_CHOICES = (
        (AM, 'AM'),
        (PM, 'PM'),
        (OTHERS, ''),
    )

    Shift = models.CharField(
        help_text=_('When the sighting session occured'),
        max_length=2,
        choices=SHIFT_CHOICES,
        default=OTHERS,
    )

    Date = models.CharField(
        help_text=_('The date of sighting session'),
        max_length=10,
    )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    OTHERS = ''

    AGE_CHOICES = (
        (ADULT, 'Adult'),
        (JUVENILE, 'JUVENILE'),
        (OTHERS, ''),
    )

    Age = models.CharField(
        help_text=_('Whether a squirrel is an adult'),
        max_length=10,
        choices=AGE_CHOICES,
        default=OTHERS,
    )

    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'
    OTHERS = ''

    COLOR_CHOICES = (
        (GRAY, 'Gray'),
        (CINNAMON, 'Cinnamon'),
        (BLACK, 'Black'),
        (OTHERS, ''),
    )

    Primary_Fur_Color = models.CharField(
        help_text=_('Primary fur color'),
        max_length=10,
        choices=COLOR_CHOICES,
        default=OTHERS,
    )

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
