# coding: utf-8

from gi.repository import Gtk, Gio

from tramontane.core.categories import Categories


class TramontaneApp(Gtk.Application):

    def __init__(self, **kwargs):
        super().__init__(application_id="github.io.tramontane", **kwargs)

        self.window = None

    def do_startup(self):
        Gtk.Application.do_startup(self)

        action = Gio.SimpleAction.new("quit", None)
        action.connect("activate", self.on_quit)
        self.add_action(action)

    def init_categories(self, listbox):
        c = Categories()
        for category in c.items:
            listbox.add(category.render())

    def do_activate(self):
        if not self.window:
            # using glade to load the ui
            builder = Gtk.Builder()
            builder.add_from_file('tramontane.glade')
            main_window = builder.get_object('applicationwindow1')
            main_window.set_application(self)

            # Build list of categories
            listbox = builder.get_object('listbox2')
            self.init_categories(listbox)

            # Main window
            self.window = main_window
            self.window.show_all()
        self.window.present()

    def on_quit(self):
        self.quit()
