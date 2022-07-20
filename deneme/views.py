from django.shortcuts import render
from django.http import HttpResponse


def deneme(request):
    return HttpResponse("<h1>Successfully tried")

# Create your views here.
