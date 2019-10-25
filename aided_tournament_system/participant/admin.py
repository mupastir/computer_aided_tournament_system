from django.contrib import admin
from .models import Player, Team


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass
