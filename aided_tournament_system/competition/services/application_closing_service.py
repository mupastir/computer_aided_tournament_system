from uuid import UUID

from competition.models import Competition


class ApplicationClosingService:

    def __init__(self, competition_id: UUID):
        self.competition_id = competition_id
        self.competition = self._get_competition()

    def _get_competition(self) -> Competition:
        return Competition.objects.get(id=self.competition_id)

    def close(self):
        self.competition.applications.update(is_open=False)
