# coding: utf-8

from gi.repository import Gtk


class FluxView:

    def __init__(self):
        #self.widget = Gtk.ListBox()
        self.widget = Gtk.TreeView()
        self.widget.set_activate_on_single_click(True)
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Title", renderer, text=0)
        self.widget.append_column(column)
        #self.widget.connect("row-selected", self.on_row_selected)