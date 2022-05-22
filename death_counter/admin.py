from django.contrib import admin
from .models import Game, Boss, Death
# Register your models here.
admin.site.register(Game)
admin.site.register(Boss)
admin.site.register(Death)