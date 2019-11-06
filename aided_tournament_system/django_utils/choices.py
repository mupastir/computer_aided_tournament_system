from enum import Enum


class ChoiceMixin:
    def __new__(cls, value, text=None):
        inst = super().__new__(cls, value)
        if isinstance(value, ChoiceMixin):
            text = value.text
        inst.text = text
        return inst


class BaseChoices(Enum):

    @classmethod
    def get_choices(cls) -> tuple:
        return tuple((i.value, i.value.text) for i in cls)


class IntChoice(ChoiceMixin, int):
    pass


class StrChoice(ChoiceMixin, str):
    pass
