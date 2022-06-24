from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.forms import inlineformset_factory
from .forms import GameForm, DeathForm, CreateUserForm, BossForm
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
    form = DeathForm(instance=player, initial={'game':game, 'player':player, 'deaths':deaths})
    form.fields['boss_name'].queryset = Boss.objects.filter(game=pk)
    if request.method == 'POST':
        form = DeathForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/death_counter/stats/'+pk)

    context = {'game':game, 'player':player, 'deaths':deaths, 'form': form}
    return render(request, 'death_counter/death_form.html', context)
def game_boss(request, pk):
    game = Game.objects.get(id=pk)
    form = BossForm(instance=game, initial={'game':game})
    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = BossForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/death_counter/stats/'+pk)
    context = {'form': form}
    return render(request, 'death_counter/game_boss.html', context)