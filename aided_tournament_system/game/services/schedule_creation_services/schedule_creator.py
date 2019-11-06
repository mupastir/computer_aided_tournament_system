from uuid import UUID

from game.services.schedule_creation_services.tournament_schedules import \
    SCHEDULE_SIZES_AVAILABLE


class ScheduleCreator:

    def __init__(self, schedule_size: str, competition_id: UUID):
        self.schedule_size = schedule_size
        self.competition_id = competition_id
        self.schedule_creator = SCHEDULE_SIZES_AVAILABLE.get(
            self.schedule_size
        )

    @property
    def schedule_size(self):
        return self._schedule_size

    @schedule_size.setter
    def schedule_size(self, value):
        self._validate_schedule_size(value)
        self._schedule_size = value

    @staticmethod
    def _validate_schedule_size(schedule_size):
        if schedule_size not in SCHEDULE_SIZES_AVAILABLE.keys():
            raise ValueError

    def create_schedule(self):
        self.schedule_creator(self.competition_id).create_games_schedule()
