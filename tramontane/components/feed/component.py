# coding: utf-8

from .model import FeedItem, FeedListStore
from .view import FeedListView


class FeedComp:

    def __init__(self):
        super().__init__()
        self.view = FeedListView()
        self.model = FeedListStore()
        self.view.widget.bind_model(self.model, self.view.get_item_widget)
        self.focus = None

    def on_cache_changed(self, cache, arg):
        print(cache.data)

    def on_category_changed(self, treeview, path, column):
        print("category changed")

    def on_selection(self, selection):
        self.model.remove_all()
        model, treeiter = selection.get_selected()
        if treeiter != None:
            item = model[treeiter][1]
            for feed in item.feeds:
                self.model.append(FeedItem(feed))