# coding: utf-8

from gi.repository import Gtk


class TCoreView:

    def __init__(self):
        self.init_view()

    def init_view(self):
        pass


class VCategoriesListView(TCoreView):

    def __init__(self, store):
        super().__init__()
        #self.widget = Gtk.ListBox()
        self.widget = Gtk.TreeView(store)
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Title", renderer, text=0)
        self.widget.append_column(column)
        #self.widget.connect("row-selected", self.on_row_selected)

    def on_item_click(self, item):
        print("lolilol")

    def on_row_selected(self, listbox, row, **kw):
        print(kw)
        print("row selected !!")

    def add_list(self, items):
        print("lol")