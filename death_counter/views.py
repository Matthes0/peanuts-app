from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def stats(request):
    return render(request, 'death_counter/stats.html')
