from django import template
from ..models import *
register = template.Library()

@register.simple_tag(name="deaths_boss")
def deaths_boss(death, player, boss):
    try:
        return death.filter(boss_name=boss).filter(player=player).distinct().values_list('deaths')[0][0]
    except IndexError:
        return ""
