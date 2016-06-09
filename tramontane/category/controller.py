# coding: utf-8

from gi.repository import Gtk, GObject

from tramontane.category.model import MItem

class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.widget.bind_model(self.model, get_item_widget)
        self.init_items()

    def init_items(self):
        self.model.append(MItem("lolilol"))


def get_item_widget(item):
    print("lol")
    row_box = Gtk.ListBoxRow()
    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    row_box.add(vbox)
    label1 = Gtk.Label(item.label, xalign=0)
    vbox.pack_start(label1, True, True, 0)
    return row_box