from django.urls import path, include

from polenovo import views
app_name='users'
urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]