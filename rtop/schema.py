from __future__ import annotations


class Row:
    def __init__(self: Row,
                 name: str,
                 attr_name: str,
                 fmt: callable = str,
                 padding: int = 4):
        self.name = name
        self.attr_name = attr_name
        self.fmt = fmt
        self.width = len(name)
        self.padding = padding

    def update(self: Row, obj: any):
        updated = False
        attr_str = self.fmt(getattr(obj, self.attr_name))
        if(len(attr_str) > self.width):
            self.width = len(attr_str)
            updated = True
        return updated

    def render_header(self: Row) -> str:
        return self.name.ljust(self.width + self.padding)

    def render(self: Row, obj: any) -> str:
        return self.fmt(getattr(obj, self.attr_name)) \
                    .ljust(self.width + self.padding, ' ')
