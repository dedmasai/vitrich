from django.urls import path

from polenovo import views

urlpatterns = [
    path('', views.index, name='index'),

]