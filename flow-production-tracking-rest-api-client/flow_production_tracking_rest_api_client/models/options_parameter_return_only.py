from enum import Enum


class OptionsParameterReturnOnly(str, Enum):
    ACTIVE = "active"
    RETIRED = "retired"

    def __str__(self) -> str:
        return str(self.value)
