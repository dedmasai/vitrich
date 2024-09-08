from django.forms import ModelForm
from .models import PlantsImport

class PlantImportForm(ModelForm):
    class Meta:
        model = PlantsImport
        fields = ('csv_file',)