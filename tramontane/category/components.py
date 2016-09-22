# coding: utf-8

from tramontane.category.model import MCategories, MItem
from tramontane.category.view import VCategoriesListView, FeedListView
from gi.repository import Gio, GObject, Gtk


class Component:

    def __init__(self):
        pass


class CategoryComp(Component):

    def __init__(self, cache):
        super().__init__()
        self.view = VCategoriesListView()
        self.model = Gtk.TreeStore(str)
        self.view.widget.set_model(self.model)

        # Signals
        cache.connect('cache_changed', self.on_cache_changed)

    ############
    # CONFIG
    ############

    def _build_node(self, treeiter, item):
        items = item.get('items', [])
        for item in items:
            new_treeiter = self.model.append(treeiter, [item['name']])
            self._build_node(new_treeiter, item)

    ############
    # CALLBACKS
    ############

    def on_cache_changed(self, cache, arg):
        self.model.clear()
        self._build_node(None, cache.data)


class FeedListComp(Component):

    def __init__(self, cache):
        super().__init__()
        self.view = FeedListView()
        self.model = MCategories()
        self.view.widget.bind_model(self.model, self.view.get_item_widget)
        self.model.append(MItem('lol'))
        self.model.append(MItem('mdr'))
        # Signals
        cache.connect('cache_changed', self.on_cache_changed)

    def on_cache_changed(self, cache, arg):
        self.model.append(MItem('mdr2'))

        row_box = Gtk.ListBoxRow()
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        row_box.add(vbox)
        label1 = Gtk.Label("lala", xalign=0)
        vbox.pack_start(label1, True, True, 0)
        self.view.widget.add(row_box)