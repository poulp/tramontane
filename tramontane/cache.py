# coding: utf-8

from gi.repository import GObject, Gio, Gtk
import json

class Cache(GObject.GObject):

    __gsignals__ = {
        'cache_changed': (
            GObject.SIGNAL_RUN_FIRST,
            None,
            (int,))
    }

    def do_cache_changed(self, arg):
        pass

    title = GObject.property(type=str, default='default title')

    def __init__(self):
        GObject.GObject.__init__(self)
        self.data = {}

    def refresh(self):
        with open('conf.json') as data_file:
            data = json.load(data_file)
        self.data = data
        self.build_cache(self.data)
        self.emit("cache_changed", 42)

    def build_cache(self, item):
        if item['type'] == 'directory':
            for item in item.get('items', []):
                item['feeds'] = []
                self.build_cache(item)
        elif item['type'] == 'feed':
            item['feeds'] = ["feed1", "feed2"]