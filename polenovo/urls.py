from django.urls import path

from polenovo import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cl', views.cl_view, name='cl'),
    path('test', views.test_view, name='test'),

]