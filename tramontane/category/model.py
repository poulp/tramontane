# coding: utf-8

from gi.repository import GObject, Gio
import json

class MCategoryItem:

    def __init__(self, text, items):
        self.label = text
        self.items = items

    def get_label(self):
        return self.label


class MItem(GObject.GObject):

    def __init__(self, label):

        GObject.GObject.__init__(self)
        self.label = label
        self.type = type


class MCategories(Gio.ListStore):

    def get_item_type(self):
        return MItem


class Cache(GObject.GObject):

    __gsignals__ = {
        'cache_changed': (
            GObject.SIGNAL_RUN_FIRST,
            None,
            (int,))
    }

    def do_cache_changed(self, arg):
        print("class method for `cache_changed' called with argument", arg)

    title = GObject.property(type=str, default='default title')

    def __init__(self):
        GObject.GObject.__init__(self)
        self.data = {}

    def init_items(self):
        with open('conf.json') as data_file:
            data = json.load(data_file)
        self.data = data
        self.emit("cache_changed", 42)