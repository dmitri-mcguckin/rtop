# RTop

[![license](https://img.shields.io/github/license/dmitri-mcguckin/rtop)](./LICENSE)
[![pypi](https://img.shields.io/pypi/v/rtop)](https://pypi.org/project/rtop)
[![issues](https://img.shields.io/github/issues/dmitri-mcguckin/rtop/bug?label=issues)](https://github.com/dmitri-mcguckin/rtop/labels/bug)
[![unit tests](https://img.shields.io/github/workflow/status/dmitri-mcguckin/rtop/Unit%20Tests?label=unit%20tests)](https://github.com/dmitri-mcguckin/rtop/actions?query=workflow%3A%22Unit+Tests%22)
[![deployment](https://img.shields.io/github/workflow/status/dmitri-mcguckin/rtop/Deploy%20to%20PyPi?label=deployment)](https://github.com/dmitri-mcguckin/rtop/actions?query=workflow%3A%22Deploy+to+PyPi%22)


A TUI monitor that integrates with [RocketLaunch.live](https://www.rocketlaunch.live) to bring a list of upcoming launches.

*(Support Rocket Launch Live [here](https://www.rocketlaunch.live/premium))*

# Quick Start

### Install

`$` `pip install rtop`

#### Start the monitor

`$` `rtop`

# Development and Contribution

### Documentation

`$` `make -C docs clean html`

### Install Locally

`$` `pip install -e .[dev]`

*(Note: the `-e` flag creates a symbolic-link to your local development version. Set it once, and forget it)*

### Run Unit Tests

`$` `python3 -m unittest tests/spec_*.py`
