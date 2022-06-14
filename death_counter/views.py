from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.forms import inlineformset_factory
from .forms import GameForm, DeathForm, CreateUserForm
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
def death_form(request, pk, ppk):
    game = Game.objects.get(id=pk)
    player = User.objects.get(id=ppk)
    deaths = Death.objects.filter(game=game).filter(player=player)
    form = DeathForm(instance=player)
    # deathFormset = DeathForm(queryset=Death.objects.none(), instance=deaths)
    if request.method == 'POST':
        form = DeathForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'game':game, 'player':player, 'deaths':deaths, 'form': form}
    return render(request, 'death_counter/death_form.html', context)
def game_boss(request, pk):

    context = {}
    return render(request, 'death_counter/game_boss.html', context)