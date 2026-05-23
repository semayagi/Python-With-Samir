import datetime
from dataclasses import dataclass


@dataclass(frozen=True)
class Task:
    task_name: str
    task_date: datetime.datetime
    task_type: str


@dataclass(frozen=True)
class FileTask:
    task_name: str
    task_date: datetime.datetime
    task_type: str
    filename: str
