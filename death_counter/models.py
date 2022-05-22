from django.db import models

# Create your models here.
class Game(models.Model):
    game_name = models.CharField(max_length=200)
class Boss(models.Model):
    boss_name = models.CharField(max_length=200)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
class Deaths(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    boss_name = models.ForeignKey(Boss, on_delete=models.CASCADE)
    deaths = models.IntegerField(default=0)