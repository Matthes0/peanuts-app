from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
def stats(request):
    games = Game.objects.all()
    context = {'games':games}
    return render(request, 'death_counter/stats.html', context)
def game(request, pk):
    game = Game.objects.get(id=pk)
    players = User.objects.all()
    bosses = Boss.objects.filter(game=game)
    deaths = Death.objects.filter(game=game)
    context = {'game':game, 'players':players, 'deaths':deaths, 'bosses':bosses}
    return render(request, 'death_counter/game.html', context)
