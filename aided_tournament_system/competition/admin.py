from django.contrib import admin

from .models import Application, Competition, Ranking


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    pass


@admin.register(Ranking)
class RankingAdmin(admin.ModelAdmin):
    pass


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    pass
