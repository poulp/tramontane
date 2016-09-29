# coding: utf-8

from .model import FluxItem, FluxTreeStore
from .view import FluxView


class FluxComp:

    def __init__(self):
        super().__init__()
        self.view = FluxView()
        self.model = FluxTreeStore(str, FluxItem)
        self.view.widget.set_model(self.model)

    ############
    # CONFIG
    ############

    def _build_node(self, treeiter, item):
        items = item.get('items', [])
        for item in items:
            item_object = FluxItem(item['name'], item['feeds'])
            new_treeiter = self.model.append(treeiter, [item_object.label, item_object])
            self._build_node(new_treeiter, item)

    ############
    # CALLBACKS
    ############

    def on_cache_changed(self, cache, arg):
        self.model.clear()
        self._build_node(None, cache.data)