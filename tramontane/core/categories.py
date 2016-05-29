# coding: utf-8

from gi.repository import Gtk


class CategoryItem:

    def __init__(self, text):
        self.label = text

    def render(self):
        row = Gtk.ListBoxRow()
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        row.add(vbox)
        label1 = Gtk.Label(self.label, xalign=0)
        vbox.pack_start(label1, True, True, 0)
        return row


class Categories:

    def __init__(self):
        self.items = [CategoryItem("New"), CategoryItem("Starred")]
