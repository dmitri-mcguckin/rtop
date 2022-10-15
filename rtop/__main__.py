# import argparse
# import time
import oresat_tpane
# from .pane import Pane
# from .launch_table import LaunchTable


def main():
    pane = Pane('Upcoming Launches')
    event_loop = urwid.MainLoop(pane)
    event_loop.run()


if __name__ == '__main__':
    main()
