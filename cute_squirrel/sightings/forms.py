from django.forms import ModelForm

from .models import squirrel

class SqForm(ModelForm):
    class Meta:
        model = squirrel
        fields = '__all__'
