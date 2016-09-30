# coding: utf-8

from gi.repository import GObject, Gtk


class FluxItem(GObject.GObject):

    def __init__(self, label, feeds):
        GObject.GObject.__init__(self)
        self.label = label
        self.feeds = feeds


class FluxTreeStore(Gtk.TreeStore):
    pass