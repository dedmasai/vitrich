from django.forms import ModelForm, forms, ChoiceField, BooleanField
from .models import CheckList, Plants


class CLForm(forms.Form):
    # create new form object from database question object
    CHOICES = (
        ('Н', 'Не определено'),
        ('В', 'До вида'),
        ('С', 'До семейства'),
         )
    vid=BooleanField(initial=False)
    fam = BooleanField(initial=False)
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
        self.success = 'Не определено'
        self.team = team
