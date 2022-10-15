from __future__ import annotations
import urwid


class Pane(urwid.WidgetContainerMixin):
    def __init__(self: Pane, name: str):
        self.name = urwid.Text(name)

    def render(self: Pane, size: tuple, focus: bool = False) -> urwid.Canvas:
        self.name.render((size[0],))
        return urwid.SolidCanvas('-', size[0], size[1])
