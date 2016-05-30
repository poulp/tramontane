# coding: utf-8

from gi.repository import Gtk


class TCoreView:

    class Meta:
        view = None

    def __init__(self, tobject):
        self.tobject = tobject
        self.view = self.Meta.view()
        self.init_view()

    def init_view(self):
        pass

    def get_view(self):
        return self.view


class CategorieItemView(TCoreView):

    class Meta:
        view = Gtk.ListBoxRow

    def init_view(self):
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.view.add(vbox)
        label1 = Gtk.Label(self.tobject.get_label(), xalign=0)
        vbox.pack_start(label1, True, True, 0)


class CategoriesListView(TCoreView):

    class Meta:
        view = Gtk.ListBox

    def init_view(self):
        items = self.tobject.items  # model items
        for item in items:
            self.view.add(CategorieItemView(item).get_view())