from django.urls import path
from . import views

urlpatterns = [
    path('stats/', views.stats, name='stats'),
    path('stats/<str:pk>', views.game, name='game'),
    path('stats/<str:pk>/game_boss', views.game_boss, name='game_boss'),
    path('stats/<str:pk>/<str:ppk>', views.death_form, name='death_form'),
]