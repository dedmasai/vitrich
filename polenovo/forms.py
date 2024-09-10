from django import forms
from django.forms import IntegerField, BooleanField
from .models import CheckList, Plants


class CLForm(forms.Form):
    # create new form object from database question object
    CHOICES = (
        ('Н', 'Не определено'),
        ('В', 'До вида'),
        ('С', 'До семейства'),
         )


    plantQ = Plants()
    def __init__(
            self,
            plantQ,
            plant,
            team,
            ):
        super().__init__()
        self.plantQ = plantQ
        self.plant = plant
        self.team = team
        self.suc = IntegerField(initial=0, required=False)
class Test_Form(forms.Form):
    class Meta:
        model = CheckList
        fields = ['vid','fam']
        labels = {
            'vid': 'Вид:',
            'fam': 'Семейство:'
        }
    fam=forms.BooleanField(initial=False,required=False)
    vid=forms.BooleanField(initial=False,required=False)