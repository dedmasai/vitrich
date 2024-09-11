from django.urls import path, include

from polenovo import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cl', views.cl_view, name='cl'),
    path('test', views.test_view, name='test'),
    path('chv',views.HomeView.as_view(), name='home'),

]