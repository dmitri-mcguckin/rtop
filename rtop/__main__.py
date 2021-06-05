# import argparse
import time
from .app import App
from .launch_table import LaunchTable


def main():
    # parser = argparse.ArgumentParser(prog=APP_NAME,
    #                                  description=APP_DESCRIPTION,
    #                                  allow_abbrev=False)
    # args = parser.parse_args()

    try:
        launch_table = LaunchTable()

        with App(launch_table) as app:
            app.draw()

            while True:
                launch_table.update()
                app.draw()
                time.sleep(0.001)
    except KeyboardInterrupt:
        print('Exiting...')
    finally:
        print('Goodbye!')


if __name__ == '__main__':
    main()
