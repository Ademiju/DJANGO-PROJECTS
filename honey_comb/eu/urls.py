from django.http import HttpResponse
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.eu_login),
    path('register/', views.eu_register)
]