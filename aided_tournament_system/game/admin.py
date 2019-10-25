from django.contrib import admin

from .models import BaseGame


@admin.register(BaseGame)
class GameAdmin(admin.ModelAdmin):
    pass
