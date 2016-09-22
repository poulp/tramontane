# coding: utf-8

from gi.repository import Gtk

from tramontane.category.model import MCategories


class TCoreView:

    def __init__(self):
        self.init_view()

    def init_view(self):
        pass


class VCategoriesListView(TCoreView):

    def __init__(self):
        super().__init__()
        #self.widget = Gtk.ListBox()
        self.widget = Gtk.TreeView()
        self.widget.set_activate_on_single_click(True)
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Title", renderer, text=0)
        self.widget.append_column(column)
        #self.widget.connect("row-selected", self.on_row_selected)


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
        return row_box