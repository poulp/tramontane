# coding: utf-8

import json

from gi.repository import Gio, GObject, Gtk

from tramontane.category.model import MCategories, MItem

CONF_FILE = 'conf.json'


def get_item_widget(item):
    row_box = Gtk.ListBoxRow()
    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    row_box.add(vbox)
    label1 = Gtk.Label(item.label, xalign=0)
    vbox.pack_start(label1, True, True, 0)
    return row_box


class Controller:

    def __init__(self, model, view, list_view):
        self.model = model
        self.view = view
        self.list_view = list_view
        # Config
        self.view.widget.connect('row_activated', self.on_row_selected)
        self.model_t = MCategories()
        list_view.bind_model(self.model_t, get_item_widget)
        self.init_items()
        self.model_t.append(MItem("test !!"))

    def init_items(self):
        with open('conf.json') as data_file:
            data = json.load(data_file)
        self.build_node(None, data)

    def build_node(self, treeiter, item):
        items = item.get('items', [])
        for item in items:
            new_treeiter = self.model.append(treeiter, [item['name']])
            self.build_node(new_treeiter, item)


    # CALLBACKS
    def on_row_selected(self, treeview, path, column):
        self.model_t.remove_all()
        from random import randint
        for i in range(0, 10):
            self.model_t.append(MItem(str(randint(0,9))))
            print(self.model_t.get_n_items())

    def get_item_widget(item):
        print("lol")
        row_box = Gtk.ListBoxRow()
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        row_box.add(vbox)
        label1 = Gtk.Label(item.label, xalign=0)
        vbox.pack_start(label1, True, True, 0)
        return row_box