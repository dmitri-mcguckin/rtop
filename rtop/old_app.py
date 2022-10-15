from __future__ import annotations
import curses
import datetime as dt
from . import trunc_timedelta, API_UPDATE_INTERVAL
from .launch_table import LaunchTable
from .schema import Row


class App:
    def __init__(self: App, launch_table: LaunchTable):
        self.launch_table = launch_table
        self.pad = None

        self.table_schema = [
            Row('Provider', 'provider'),
            Row('Vehicle', 'vehicle'),
            Row('In', 'time_until', trunc_timedelta),
            Row('At', 'location'),
            Row('Estimated Date', 'date'),
        ]

    def __init_color_pairs(self: App) -> None:
        """
        Initialize color options used by curses
        :return: None
        """
        curses.start_color()
        # Implied: color pair 0 is standard black and white
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

    def __enter__(self: App) -> App:
        # Monitor setup, take a snapshot of the terminal state
        self.screen = curses.initscr()  # Initialize standard out
        self.screen.scrollok(True)  # Enable window scroll
        self.screen.keypad(True)  # Enable special key input
        self.screen.nodelay(True)  # Disable user-input blocking
        curses.noecho()  # disable user-input echo
        curses.curs_set(False)  # Disable the cursor
        self.__init_color_pairs()  # Enable colors and create pairs

        height, width = self.screen.getmaxyx()
        self.pad = curses.newpad(height - 1, width)
        self.__init_pad()
        return self

    def __init_pad(self: App):
        self.pad.move(1, 0)
        self.pad.box()
        self.pad.addstr(0, 1, "Rocket-Top:")

    def __exit__(self: App, type, value, traceback) -> None:
        # Monitor destruction, restore terminal state
        curses.nocbreak()  # Re-enable line-buffering
        curses.echo()  # Enable user-input echo
        curses.curs_set(True)  # Enable the cursor
        curses.resetty()  # Restore the terminal state
        curses.endwin()  # Destroy the virtual screen

    def __update_schema(self: App):
        for row in self.table_schema:
            for launch in self.launch_table:
                row.update(launch)

    def __draw_banner(self: App):
        height, width = self.screen.getmaxyx()
        update_in = trunc_timedelta(API_UPDATE_INTERVAL
                                    - self.launch_table.time_until_update)
        banner = f'{dt.datetime.now().ctime()} [Update In: {update_in}]' \
                 .ljust(width, ' ')
        self.screen.addstr(0, 0, banner)
        self.screen.refresh()

    def __draw_header(self: App):
        header = ''
        line_style = curses.color_pair(4) | curses.A_REVERSE
        for row in self.table_schema:
            header += row.render_header()
        self.pad.addstr(1, 1, header, line_style)

    def draw(self: App) -> None:
        self.__update_schema()
        self.__draw_banner()
        self.__draw_header()

        height, width = self.pad.getmaxyx()

        for i, launch in enumerate(self.launch_table):
            line = ''
            line_style = curses.color_pair(3) \
                if(launch.time_until <= dt.timedelta(days=1)) \
                else curses.color_pair(0)
            for row in self.table_schema:
                line += row.render(launch)
            self.pad.addstr(2 + i, 1, line, line_style)
        self.pad.refresh(0, 0, 1, 0, height, width)
