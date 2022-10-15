from __future__ import annotations
import json
import copy
import requests
import datetime as dt
from .launch import Launch
from . import API_URI, API_UPDATE_INTERVAL


class LaunchTable:
    def __init__(self: LaunchTable):
        self.api_uri = API_URI
        self.upcoming_launches = {}
        self.past_launches = {}
        self.last_updated = dt.datetime(year=1970,
                                        month=1,
                                        day=1,
                                        hour=0,
                                        minute=0,
                                        second=0)

    def __add__(self: LaunchTable, launch: Launch):
        self.upcoming_launches[launch.id] = launch

    def __iter__(self: LaunchTable) -> LaunchTable:
        self._start = 0
        # Create a list of launch id's sorted by time-until-launch
        sorted_table = sorted(self.upcoming_launches.values(),
                              key=lambda x: x.time_until,
                              reverse=False)
        self._keys = list(map(lambda x: x.id, sorted_table))
        return self

    def __next__(self: LaunchTable) -> Launch:
        if(self._start > (len(self._keys) - 1)):
            del self._start
            del self._keys
            raise StopIteration()
        res = self.upcoming_launches[self._keys[self._start]]
        self._start += 1
        return res

    def past_launches(self: LaunchTable) -> [Launch]:
        return sorted(list(self.past_launches.values()),
                      key=lambda x: x.time_until,
                      reverse=False)

    @property
    def time_until_update(self: LaunchTable) -> dt.timedelta:
        return (dt.datetime.now() - self.last_updated)

    def update(self: LaunchTable) -> int:
        new_adds = 0

        if(self.time_until_update >= API_UPDATE_INTERVAL):
            self.last_updated = dt.datetime.now()
            http_response = requests.get(self.api_uri)

            if(http_response.status_code != 200):
                return False

            raw_data = json.loads(http_response.text)['result']
            for r in raw_data:
                launch = Launch(r)
                if(not self.upcoming_launches.get(launch.id)):
                    new_adds += 1
                self.upcoming_launches[launch.id] = launch

        upcoming = copy.deepcopy(list(self.upcoming_launches.values()))
        for launch in upcoming:
            if(launch.time_until.total_seconds() <= 0):
                self.past_launches[launch.id] = launch
                self.upcoming_launches.pop(launch.id)

        return new_adds
