from django.contrib.auth.models import User
from django.forms import formset_factory, forms
from django.shortcuts import render

# Create your views here.
from polenovo.forms import CLForm,  Test_Form
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
                suc=line.suc,
            )
            cl.save()
    else:
        lines = clformset
    context = {
        "lines": lines
    }

    return render(request, "polenovo/checklist.html", context)

def test_view(request):

    team=Team.objects.first()

    Pl = Plants.objects.first(

    )
    form=Test_Form()

    if request.method == 'POST':
        form=Test_Form(request.POST)
        if form.is_valid():
            cl=CheckList(
                team=team,
                plant=Pl,
                fam=form.cleaned_data['fam'],
                # fam=True,
                # vid=True,
                vid=form.cleaned_data['vid']
            )
            cl.save()
    else:
        form = form
    context = {
        "form": form
    }

    return render(request, "polenovo/test.html", context)
