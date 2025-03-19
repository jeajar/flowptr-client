from enum import Enum


class CreateFieldRequestDataType(str, Enum):
    CALCULATED = "calculated"
    CHECKBOX = "checkbox"
    CURRENCY = "currency"
    DATE = "date"
    DATE_TIME = "date_time"
    DURATION = "duration"
    ENTITY = "entity"
    FLOAT = "float"
    FOOTAGE = "footage"
    LIST = "list"
    MULTI_ENTITY = "multi_entity"
    NUMBER = "number"
    PERCENT = "percent"
    STATUS_LIST = "status_list"
    TEXT = "text"
    TIMECODE = "timecode"
    URL = "url"
    UUID = "uuid"

    def __str__(self) -> str:
        return str(self.value)
