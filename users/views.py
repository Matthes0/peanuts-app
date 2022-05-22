from django.shortcuts import render,redirect
from django.http import HttpResponse


def home(request):
    return render(request, 'users/home.html')
# Create your views here.
