# coding: utf-8

from gi.repository import Gtk


class View:

    class Meta:
        widget = None

    def __init__(self):
        if hasattr(self.Meta, 'widget') and self.Meta.widget:
            self.widget = self.Meta.widget()
        else:
            self.widget = self.get_view()

    def get_view(self):
        """ Return widget """
        raise NotImplementedError


class ListView(View):

    class Meta:
        widget = Gtk.ListBox

    def get_item_widget(self, item):
        raise NotImplementedError