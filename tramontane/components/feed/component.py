# coding: utf-8

from tramontane.lib.component import ListComponent
from tramontane.components.feed.model import FeedItem, FeedListStore
from tramontane.components.feed.view import FeedListView


class FeedComp(ListComponent):

    class Meta:
        view = FeedListView
        model = FeedListStore

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