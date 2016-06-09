# coding: utf-8

from gi.repository import Gtk


class TCoreView:

    def __init__(self):
        self.init_view()

    def init_view(self):
        pass


class VCategoriesListView(TCoreView):

    def __init__(self):
        super().__init__()
        self.widget = Gtk.ListBox()
        self.widget.connect("row-selected", self.on_row_selected)

    def on_item_click(self, item):
        print("lolilol")

    def on_row_selected(self, data, aa):
        print(data)
        print(aa)

    def add_list(self, items):
        print("lol")