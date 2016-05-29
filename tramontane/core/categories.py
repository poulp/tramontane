# coding: utf-8

from gi.repository import Gtk


class TramontaneObject:

    # class Meta:
    #     view = None
    #
    # def _render(self):
    #     return self.Meta.view()
    #
    # def render(self, *args, **kwargs):
    #     return self.Meta.view(*args, **kwargs)

    def __init__(self, meta):
        self.meta = meta


class CategoryItem:

    def __init__(self, text):
        self.label = text

    def get_label(self):
        return 'lol{}'.format(self.label)


class Categories:

    def __init__(self):
        self.items = [CategoryItem("New"), CategoryItem("Starred")]