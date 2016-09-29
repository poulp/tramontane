# coding: utf-8

from gi.repository import GObject, Gio


class FeedItem(GObject.GObject):

    def __init__(self, label):
        GObject.GObject.__init__(self)
        self.label = label


class FeedListStore(Gio.ListStore):

    def get_item_type(self):
        return FeedItem