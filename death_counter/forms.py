from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Game, Boss, Death

class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = '__all__'
class DeathForm(ModelForm):
    class Meta:
        model = Death
        fields = '__all__'
class BossForm(ModelForm):
    class Meta:
        model = Boss
        fields = '__all__'
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']