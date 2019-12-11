from uuid import UUID

from competition.models import Competition


class ApplicationClosingService:

    def __init__(self, competition_id: UUID):
        self.competition_id = competition_id

    def close(self):
        return Competition.objects.filter(
            id=self.competition_id
        ).update(is_open=False)
