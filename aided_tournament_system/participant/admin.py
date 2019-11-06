from django.contrib import admin

from .models import Player, Referee, Team


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    pass


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(Referee)
class RefereeAdmin(admin.ModelAdmin):
    pass
