# coding: utf-8

from tramontane.category.view import VCategoriesListView
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
       # self.init_items()

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
