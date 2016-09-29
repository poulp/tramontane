# coding: utf-8

from gi.repository import Gtk


class FeedListView:

    def __init__(self):
        super().__init__()
        self.widget = Gtk.ListBox()

    def get_item_widget(self, item):
        row_box = Gtk.ListBoxRow()
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        row_box.add(vbox)
        label1 = Gtk.Label(item.label, xalign=0)
        vbox.pack_start(label1, True, True, 0)
        row_box.show_all()
        return row_box
