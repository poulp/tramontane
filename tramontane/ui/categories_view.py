# coding: utf-8

from gi.repository import Gtk


class TCoreView:

    class Meta:
        model = None

    def __init__(self, meta):
        self.meta = meta


class CategorieItemView(Gtk.ListBoxRow, TCoreView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(vbox)
        label1 = Gtk.Label(self.meta.get_label, xalign=0)
        vbox.pack_start(label1, True, True, 0)


class CategoriesListView(Gtk.ListBox, TCoreView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.init_list()

    def init_list(self):
        items = self.meta.items # model items
        for item in items:
            self.add(CategorieItemView(item))