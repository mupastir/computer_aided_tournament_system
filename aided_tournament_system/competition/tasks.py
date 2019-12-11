from __future__ import absolute_import, unicode_literals

from uuid import UUID

from celery import shared_task
from competition.services.application import ApplicationClosingService
from competition.services.ranking import ranking_creating_service
from competition.services.seeding_teams_service import SeedingTeamsService
from game.services.schedule_creation_services.schedule_creator import \
    ScheduleCreator
from participant.services.team import team_rating_calculate


@shared_task
def application_closing_task(competition_id: UUID):
    application_closing_service = ApplicationClosingService(competition_id)
    application_closing_service.close()


@shared_task
def ranking_creation_task(competition_id: UUID):
    ranking_creating_service(competition_id)


@shared_task
def schedule_creating_task(competition_id: UUID,
                           competition_schedule_system: str):
    schedule_creator = ScheduleCreator(competition_schedule_system,
                                       competition_id)
    schedule_creator.create_schedule()


@shared_task
def seeding_teams_task(competition_id: UUID):
    seeding_teams_service = SeedingTeamsService(competition_id)
    seeding_teams_service.seed()


@shared_task
def calculate_team_rating_task(team_id: UUID, competition_type: str):
    team_rating_calculate(team_id, competition_type)
