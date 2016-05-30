# coding: utf-8

from gi.repository import Gtk, Gio

from tramontane.core.categories import Categories
from tramontane.ui.categories_view import CategoriesListView


class TramontaneGtkApplicationWindow(Gtk.ApplicationWindow):

    default_title = "Tramontane"
    default_width = 800
    default_height = 600

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_title(TramontaneGtkApplicationWindow.default_title)
        self.set_default_size(
            TramontaneGtkApplicationWindow.default_width,
            TramontaneGtkApplicationWindow.default_height
        )

        hbox = Gtk.HBox()
        categories = CategoriesListView(Categories())
        hbox.pack_start(categories.get_view(), True, True, 0)
        categories = CategoriesListView(Categories())
        hbox.pack_start(categories.get_view(), True, True, 0)
        self.add(hbox)


class TramontaneApp(Gtk.Application):

    def __init__(self, **kwargs):
        super().__init__(application_id="github.io.tramontane", **kwargs)
        self.window = None

    def do_startup(self):
        Gtk.Application.do_startup(self)

        action = Gio.SimpleAction.new("quit", None)
        action.connect("activate", self.on_quit)
        self.add_action(action)

    def do_activate(self):
        if not self.window:
            # Main window
            self.window = TramontaneGtkApplicationWindow(application=self)
            self.window.show_all()
        self.window.present()

    def on_quit(self):
        self.quit()
