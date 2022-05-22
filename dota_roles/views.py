from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Dota 2 roles")
# Create your views here.
