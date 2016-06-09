# coding: utf-8

from gi.repository import GObject, Gio

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


class MCategories(Gio.ListStore):
    def get_item_type(self):
        return MItem