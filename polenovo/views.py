from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.forms import formset_factory, forms, BooleanField, modelformset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from polenovo.forms import CLForm, Test_Form, LoginUserForm
from polenovo.models import Plants, CheckList, Team


def index(request):
    return render(request,'polenovo/index.html')

def cl_view(request):


    Formset=modelformset_factory(CheckList,fields=('N','fam','vid'))

    if request.method == 'POST':
        form=Formset(request.POST)
        form.save()
        return redirect("index")
    else:
        team = Team.objects.first()
        rawPl = Plants.objects.all()
        for pl in rawPl:
            cl = CheckList(
                team=team,
                plant=pl,
                N=pl.title
            )
            cl.save()

    form = Formset()
    context = {
        "form": form
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
                vid=form.cleaned_data['vid']
            )
            cl.save()
    else:
        form = form
    context = {
        "form": form
    }

    return render(request, "polenovo/test.html", context)


def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = LoginUserForm()
    return render(request, 'users/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))