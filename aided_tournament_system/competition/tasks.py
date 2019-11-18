from __future__ import absolute_import, unicode_literals

from uuid import UUID

from celery import shared_task
from competition.services.application_closing_service import \
    ApplicationClosingService
from competition.services.ranking_creating_service import ranking_create
from competition.services.seeding_teams_service import SeedingTeamsService


@shared_task
def application_closing_task(competition_id: UUID):
    application_closing_service = ApplicationClosingService(competition_id)
    application_closing_service.close()


@shared_task
def ranking_creation_task(competition_id: UUID):
    ranking_create(competition_id)


@shared_task
def seeding_teams_task(competition_id: UUID):
    seeding_teams_service = SeedingTeamsService(competition_id)
    seeding_teams_service.seed()
