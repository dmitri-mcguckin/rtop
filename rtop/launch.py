from __future__ import annotations
import datetime as dt
from . import trunc_timedelta


class Launch:
    def __init__(self: Launch, data: dict = {}):
        self.id = data['id']
        self.name = data['name']
        self.description = data['launch_description']
        self.location = data['pad']['location']['name']
        self.provider = data['provider']['name']
        self.vehicle = data['vehicle']['name']
        self.date = dt.datetime.fromtimestamp(int(data['sort_date']))

    def __str__(self: Launch) -> str:
        return f'{self.date.ctime()}' \
               f' {self.provider}\'s' \
               f' {self.vehicle}' \
               f' at {self.location}' \
               f' (in {trunc_timedelta(self.time_until)})'

    @property
    def time_until(self: Launch) -> dt.timedelta:
        return -1 * (dt.datetime.now() - self.date)
