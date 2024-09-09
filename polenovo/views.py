from django.contrib.auth.models import User
from django.forms import formset_factory, forms
from django.shortcuts import render

# Create your views here.
from polenovo.forms import CLForm
from polenovo.models import Plants, CheckList, Team


def index(request):
    return render(request,'polenovo/index.html')

def cl_view(request):

    team=Team.objects.first()

    rawPl = Plants.objects.all()

    clformset = []
    for item in rawPl:
        line_in_list = CLForm(
            plantQ=item,
            plant=item.title,
            team=team,
        )
        clformset.append(line_in_list)

    if request.method == 'POST':
        lines = clformset
        for line in lines:
            cl = CheckList(
                team=team,
                plant=line.plantQ,
                success=line.success,
            )
            cl.save()
    else:
        lines = clformset
    context = {
        "lines": lines
    }

    return render(request, "polenovo/checklist.html", context)
