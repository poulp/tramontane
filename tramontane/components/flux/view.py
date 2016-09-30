# coding: utf-8

from gi.repository import Gtk

from tramontane.lib.view import View


class FluxView(View):

    class Meta:
        widget = Gtk.TreeView

    def __init__(self):
        super().__init__()
        self.widget.set_activate_on_single_click(True)
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Title", renderer, text=0)
        self.widget.append_column(column)
