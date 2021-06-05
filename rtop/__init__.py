import os
import datetime as dt

MAJOR = 0
MINOR = 0
PATCH = 1

APP_NAME = 'rtop'
APP_AUTHOR = ' Dmitri McGuckin'
APP_DESCRIPTION = 'A TUI monitor that integrates with RocketLaunch.live to' \
                  ' bring a list of upcoming launches.'
APP_VERSION = f'{MAJOR}.{MINOR}.{PATCH}'
APP_LICENSE = 'GPL-3.0'
APP_URL = 'https://github.com/dmitri-mcguckin/rtop'

API_UPDATE_INTERVAL = dt.timedelta(minutes=1)
API_URI = 'https://fdo.rocketlaunch.live/json/launches/next/5'
# API_URI = 'http://localhost:3000/api'

CACHE_DIR = os.path.expanduser('~/.cache/rtop')


def trunc_timedelta(time: dt.timedelta) -> str:
    if(abs(int(time.total_seconds() / 86400)) > 1):
        return f'{int(time.total_seconds() / 86400)}d'
    elif(abs(int(time.total_seconds() / 3600)) > 1):
        return f'{int(time.total_seconds() / 3600)}h'
    elif(abs(int(time.total_seconds() / 60)) > 1):
        return f'{int(time.total_seconds() / 60)}m'
    else:
        return f'{int(time.total_seconds())}s'
