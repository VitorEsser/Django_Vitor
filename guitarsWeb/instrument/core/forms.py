from django.forms import ModelForm
from .models import Instrument

class InstrumentForm(ModelForm):

    class Meta:
        model = Instrument
        fields = ['name', 'brands', 'strings', 'photo']
