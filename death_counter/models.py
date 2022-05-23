from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Game(models.Model):
    game_name = models.CharField(max_length=200)

    #return game name
    def __str__(self):
        return self.game_name

class Boss(models.Model):
    boss_name = models.CharField(max_length=200)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    #return boss name
    def __str__(self):
        return self.boss_name

    #proper plural
    class Meta:
        verbose_name_plural = "Bosses"

class Death(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    boss_name = models.ForeignKey(Boss, on_delete=models.CASCADE)
    deaths = models.IntegerField(default=0)
    player = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    #return death count
    def __str__(self):
        return self.deaths