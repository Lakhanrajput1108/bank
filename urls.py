from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('',views.register, name='register'),
    path('register/',views.register),
    path("login", views.login, name="login"),
    ]
 