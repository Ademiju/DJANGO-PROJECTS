from django.http import HttpResponse
from django.shortcuts import render


def ng_login(request):
    return render(request, "login.html",context={"country": "Nigerians"})

def ng_register(request):
    return render(request,"register.html", context={"country": "Nigerians"})
# Create your views here.
