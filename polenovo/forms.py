from django import forms
from django.forms import IntegerField, BooleanField
from .models import CheckList, Plants


class CLForm(forms.Form):
    # create new form object from database question object
    def __init__(
            self,
            team,
            plantC,
            plantT,
            fam,
            vid,
    ):
        super().__init__()
        self.fam = fam
        self.vid = vid
        self.plantC = plantC
        self.plantT = plantT
        self.team = team







class Test_Form(forms.Form):
    # class Meta:
    #     model = CheckList
    #     fields = ['vid','fam']
    #     labels = {
    #         'vid': 'Вид:',
    #         'fam': 'Семейство:'
    #     }
    fam=forms.BooleanField(initial=False,required=False)
    vid=forms.BooleanField(initial=False,required=False)