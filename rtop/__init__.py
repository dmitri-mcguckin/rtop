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

API_UPDATE_INTERVAL = dt.timedelta(seconds=10)

CACHE_DIR = os.path.expanduser('~/.cache/rtop')
