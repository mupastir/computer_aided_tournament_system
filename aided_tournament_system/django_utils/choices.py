from enum import Enum


class BaseChoices(Enum):

    @classmethod
    def get_choices(cls):
        choices = []
        for _cls in cls.mro():
            if _cls is not object:
                choices.extend(choice.value for choice in _cls)
        return choices
