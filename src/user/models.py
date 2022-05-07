from datetime import date, datetime

from pydantic import BaseModel, validator


class StatsAddV12(BaseModel):
    id: int
    answer: str
    question: str
    date: date

    @validator("date", pre=True)
    def parse_date(cls, value):
        if type(value) is datetime:
            return value.date()
        if type(value) is date:
            return value
        return datetime.strptime(
            value[0:19],
            "%Y-%m-%dT%H:%M:%S"
        ).date()


class StatsAddV1(BaseModel):
    questions_num: int

