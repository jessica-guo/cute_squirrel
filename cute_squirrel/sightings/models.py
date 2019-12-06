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


# Create your models here.
