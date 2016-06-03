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

    def set_list(self, items):
        for item in items:
            self.add_item(item.get_label())

    def add_item(self, item_label):
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.widget.add(vbox)
        label1 = Gtk.Label(item_label, xalign=0)
        vbox.pack_start(label1, True, True, 0)

    def add_list(self, lst):
        pass
